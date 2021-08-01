import torch.nn as nn
from functools import reduce


# 根据用户当前节点的向量(512维), 提供一个用户下一个节点应该处在的向量
class User_Individualize(nn.Module):
    def __init__(self):
        super(User_Individualize, self).__init__()
        self.relu = [
            nn.RReLU(lower=0.0125, upper=0.025, inplace=False)
            for in range(6)
        ]
        self.linear_reLu_stack = [
            self.relu[i](nn.Linear(in_features=512, out_features=512))
            for i in range(6)
        ]
        pass

    def forward(self, inputs):
        return reduce(lambda x, f: f(x), self.linear_reLu_stack, inputs)