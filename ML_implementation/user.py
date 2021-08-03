import torch
import torch.nn as nn


class User(nn.Module):
    def __init__(self):
        super().__init__()
        self.lin_relu_stk = nn.Sequential(
            *[nn.Sequential(
                nn.Linear(512, 512, bias=True),
                nn.RReLU())
              for x in range(2)]
        )
        self.shortcut = nn.Sequential()

    def forward(self, inputs):
        outputs = self.lin_relu_stk(inputs) + self.shortcut(inputs)
        return outputs


if __name__ == '__main__':
    # 模块测试
    print("\n", "=" * 10, "执行模块测试任务", "=" * 10)

    # 设备信息
    device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
    print(" " * 4, "设备为", device.type)

    # 模型、损失函数、优化器
    user1 = User().to(device)
    loss_func = nn.MSELoss().to(device)
    optimzer = torch.optim.SGD(user1.parameters(), lr=1e-3, momentum=0.9)

    # 随机生成拟合任务
    import random
    rand_power = random.random() * 2
    rand_wei = random.random() * 3 - 1.5
    print(
        " " * 4, '拟合逐分量映射 f: x → x**%.3f + (%.3f)*x, x∈ [0,1)' %
        (rand_power, rand_wei))

    # 训练过程误差
    running_loss = 0

    # 训练数据集大小
    test_size = 2 ** 20

    # 训练过程
    for x in range(test_size):
        # 直接生成数据和标签
        inputs = torch.rand(512).to(device)
        labels = inputs ** rand_power + inputs * rand_wei
        labels = labels.to(device)

        # 初始化优化器, 预测输出, 计算损失
        optimzer.zero_grad()
        outputs = user1(inputs)
        loss = loss_func(outputs, labels)

        # 更新误差(这也可以用动量ヾ(≧▽≦*)o, 没想到吧)
        running_loss += 0.1 * (loss.item() - running_loss)
        if x % 2 ** 7 == 9:
            print('\r', ' ' * 3, '运行误差 %.6f[训练进度 %.3f%%]' %
                  (running_loss, x / test_size * 100),
                  end='')

        # 误差反向传播
        loss.backward()
        optimzer.step()

    print("\n", " "*3, "最终误差 %.6f" % (running_loss))
    print("", "=" * 38)
