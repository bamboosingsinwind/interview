import torch
import torch.nn as nn
import torch.nn.functional as F
import matplotlib.pyplot as plt
import numpy as np

# 定义一个简单的一维信号模型
class SignalModel(nn.Module):
    def __init__(self):
        super(SignalModel, self).__init__()
        self.fc1 = nn.Linear(10, 5)
        self.fc2 = nn.Linear(5, 1)

    def forward(self, x):
        x = F.relu(self.fc1(x))
        x = self.fc2(x)
        return x

# 创建模型实例
model = SignalModel()

# 准备输入信号，这里简单生成一个示例输入
input_signal = torch.tensor([1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0], requires_grad=True)

# 进行前向传播
output = model(input_signal.unsqueeze(0))  # 添加unsqueeze操作以将输入信号转换为二维

# 定义要解释的类别的索引（这里只有一个输出）
class_index = 0

# 定义LRP的alpha参数
alpha = 2.0

# 定义LRP热图的计算方法
def compute_lrp_heatmap(model, input_signal, class_index, alpha):
    # 将模型的输出设置为0，除了指定的类别
    output[0, :].zero_()
    output[0, class_index] = 1.0

    # 反向传播，计算LRP热图
    model.zero_grad()
    output.backward()
    relevance = input_signal.grad * input_signal

    # 使用alpha参数进行LRP计算
    relevance = relevance / (relevance.sum() + 1e-10)
    return relevance

# 计算LRP热图
lrp_heatmap = compute_lrp_heatmap(model, input_signal, class_index, alpha)

# 将热力图数值表示为信号的颜色
plt.subplot(2, 1, 1)
plt.plot(input_signal.detach().numpy(), label='Input Signal')
plt.xlabel('Input Position')
plt.ylabel('Signal Value')

plt.subplot(2, 1, 2)
plt.imshow(lrp_heatmap.detach().numpy().reshape(1, -1), cmap='coolwarm', aspect='auto', extent=[0, 10, 0, 1])
plt.xlabel('Input Position')
plt.ylabel('Relevance')
plt.colorbar(label='Relevance Value')

plt.tight_layout()
plt.show()
