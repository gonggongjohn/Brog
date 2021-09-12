import os
from queue import Queue
import torch
import torch.nn as nn


class ResBlock(nn.Module):
    def __init__(self):
        super().__init__()
        self.lin_relu_stk = nn.Sequential(
            *[nn.Sequential(
                nn.Linear(512, 512, bias=True),
                nn.ReLU())
              for x in range(6)]
        )
        self.shortcut = nn.Sequential()

    def forward(self, inputv):
        outputv = self.lin_relu_stk(inputv) + self.shortcut(inputv)
        return outputv


class User(nn.Module):
    def __init__(self):
        super().__init__()
        self.res_block_stk = nn.Sequential(
            *[ResBlock()
                for x in range(3)]
        )

    def forward(self, inputv):
        return self.res_block_stk(inputv)


active_user = dict()
MODEL_DIR = os.path.join(os.path.dirname(__file__), "state")


class UserObj:
    def __init__(self, user_id):
        self.id = user_id
        self.path = MODEL_DIR
        self.device = torch.device(
            "cuda:0" if torch.cuda.is_available() else "cpu")
        self.user = User().to(self.device)
        self.loss_func = nn.MSELoss().to(self.device)
        self.optimizer = torch.optim.SGD(self.user.parameters(), lr=1e-6, momentum=999e-3, weight_decay=1e-3, nesterov=True)
        try:
            total_state_dict = torch.load(
                os.path.join(self.path, self.id + ".model"))
            self.user.load_state_dict(total_state_dict['model'])
            self.optimizer.load_state_dict(total_state_dict['optimizer'])
        except:
            pass
        self.inQueue = Queue()

    def forward(self, inputv):
        inputv = inputv.to(self.device)
        self.inQueue.put(inputv)
        with torch.no_grad():
            outputv = self.user.forward(inputv)
            self.user.zero_grad()
            return outputv

    def backward(self, labelv):
        labelv = labelv.to(self.device)
        inputv = self.user(self.inQueue.get())
        self.optimizer.zero_grad()
        outputv = self.user(inputv)
        loss = self.loss_func(outputv, labelv)
        loss.backward()
        loss = loss.item()
        self.optimizer.step()
        if self.inQueue.empty():
            torch.save(
                {
                    "model": self.user.state_dict(),
                    "optimizer": self.optimizer.state_dict()
                },
                os.path.join(self.path, self.id + ".model")
            )
        return loss


def getUserObj(user_id) -> UserObj:
    if user_id not in active_user:
        user_obj = UserObj(user_id)
        active_user[user_id] = user_obj
    return active_user[user_id]


if __name__ == '__main__':
    # 模块测试
    print("\n", "=" * 40, "执行模块测试任务1", "=" * 40)

    if input(" " * 48) == 'yes':
        # 设备信息
        device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
        # device = torch.device("cpu")
        print(" " * 4, "设备为", device.type)

        # 模型、损失函数、优化器
        test_user = User().to(device)
        loss_func = nn.MSELoss().to(device)
        optimizer = torch.optim.SGD(
            test_user.parameters(), lr=1e-4, momentum=0.01)

        # 随机生成拟合任务
        import random
        # rand_power = random.random() * 2 + 1
        # rand_wei = random.random() * 3 - 1.5
        # rand_bias = random.random() * 10
        rand_power = 2.5
        rand_wei = 4
        rand_bias = 9
        print(
            " " * 4, '拟合逐分量映射 f: x → x**%.3f + (%.3f)*x + (%.3f), x∈ [0,10)' %
            (rand_power, rand_wei, rand_bias))

        # 训练过程误差
        running_loss = 0

        # 训练数据集大小
        test_size = 2 ** 15

        # 训练过程
        for x in range(test_size):
            # 直接生成数据和标签
            inputv = 2 * torch.rand(512).to(device)
            labels = inputv ** rand_power + inputv * rand_wei + rand_bias
            labels = labels.to(device)

            optimizer.zero_grad()

            # 初始化优化器, 预测输出, 计算损失
            outputv = test_user(inputv)
            loss = loss_func(outputv, labels)

            # 更新误差(这也可以用动量ヾ(≧▽≦*)o, 没想到吧)
            running_loss += 0.01 * (loss.item() - running_loss)
            if x % 2 ** 6 == 9:
                print('\r', ' ' * 3, '运行误差 %.6f[训练进度 %.3f%%]' %
                      (running_loss, x / test_size * 100),
                      end='')

            # 误差反向传播
            loss.backward()
            optimizer.step()

        print("\n", " "*3, "最终误差 %.6f" % (running_loss))
    else:
        print(" " * 47, "跳过")
    print("", "=" * 99, "\n")

    print("\n", "=" * 40, "执行模块测试任务2", "=" * 40)
    if input(" " * 49) == 'yes':
        test_size = 2 ** 15
        device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")

        test_user_obj = getUserObj('test')
        test_user_obj_cp = getUserObj('test')
        print(" " * 4, "Same id get same object? ",
              test_user_obj == test_user_obj_cp)

        rand_power = 2.5
        rand_wei = 4
        rand_bias = 9
        print(
            " " * 4, '拟合逐分量映射 f: x → x**%.3f + (%.3f)*x + (%.3f), x∈ [0,1)' %
            (rand_power, rand_wei, rand_bias))

        running_loss = 0

        for x in range(0, test_size, 4):
            labels = []
            test_user_obj = getUserObj('test')

            for y in range(4):
                # 直接生成数据和标签
                inputv = 5 * torch.rand(512).to(device)
                labels.append(inputv ** rand_power +
                              inputv * rand_wei + rand_bias)
                outputv = test_user_obj.forward(inputv)

            for y in range(4):
                running_loss += 1e-2 * \
                    (test_user_obj.backward(labels[y])-running_loss)
                if (x + y) % 2 ** 6 == 9:
                    print('\r', ' ' * 3, '运行误差 %.6f[训练进度 %.3f%%]' %
                          (running_loss, (x + y) / test_size * 100),
                          end='')
    else:
        print(" " * 47, "跳过")
    print("", "=" * 99, "\n")
