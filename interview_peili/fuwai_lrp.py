import torch
import torch.nn as nn
import torch.nn.functional as F
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.cm as cm
from matplotlib.colors import Normalize
# 定义一个简单的一维信号模型
class SignalModel(nn.Module):
    def __init__(self):
        super(SignalModel, self).__init__()
        self.fc1 = nn.Linear(50, 5)
        self.fc2 = nn.Linear(5, 1)

    def forward(self, x):
        x = F.relu(self.fc1(x))
        x = self.fc2(x)
        return x

# 创建模型实例
model = SignalModel()

# 准备输入信号，这里简单生成一个示例输入
input_signal = torch.tensor(np.sin(np.linspace(1,10,50)), requires_grad=True,dtype=torch.float32)

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
    relevance = input_signal  #input_signal.grad * input_signal

    # 使用alpha参数进行LRP计算
    relevance = relevance / (relevance.sum() + 1e-10)
    return relevance

# 计算LRP热图
lrp_heatmap = compute_lrp_heatmap(model, input_signal, class_index, alpha).detach().numpy()
print("lrp",lrp_heatmap)

# 将热力图数值表示为线段的颜色
fig, ax = plt.subplots(figsize=(8, 4))
input_signal_np = input_signal.detach().numpy()

# 自定义颜色映射范围
norm = Normalize(vmin=lrp_heatmap.min(), vmax=lrp_heatmap.max())
color_map = cm.ScalarMappable(cmap='coolwarm', norm=norm)
color_map.set_array([])  # 空数组，因为norm已经定义了范围

for i in range(len(input_signal)-1):
    color = color_map.to_rgba(lrp_heatmap[i])
    plt.plot([i, i+1], [input_signal_np[i], input_signal_np[i+1]], color=color)

# 手动添加颜色条
cbar = plt.colorbar(color_map, orientation='vertical', label='Relevance Value', ax=ax)

plt.xlabel('Input Position')
plt.ylabel('Signal Value')
plt.tight_layout()
plt.savefig('./lrp_heatmap.png')
# plt.show()

# fig, ax = plt.subplots(figsize=(8, 4))
# input_signal_np = input_signal.detach().numpy()
# color_map = cm.ScalarMappable(cmap='coolwarm')
# color_map.set_array(lrp_heatmap)
# for i in range(len(input_signal)-1):
#     plt.plot([i, i+1], [input_signal_np[i], input_signal_np[i+1]], color=color_map.to_rgba(lrp_heatmap[i]))
#     print(color_map.to_rgba(lrp_heatmap[i]))
    
# # 添加颜色条
# cbar = plt.colorbar(color_map, orientation='vertical', label='Relevance Value')

# plt.xlabel('Input Position')
# plt.ylabel('Signal Value')
# plt.tight_layout()
# plt.show()


# # 将热力图数值表示为信号的颜色深浅
# fig, ax = plt.subplots(figsize=(8, 4))
# ax.plot(input_signal.detach().numpy(), label='Input Signal', color='blue')
# cax = ax.imshow(
#     lrp_heatmap.detach().numpy().reshape(1, -1),
#     cmap='coolwarm',
#     aspect='auto',
#     extent=[0, 10, 0, 1],
#     alpha=0.5,
# )
# plt.xlabel('Input Position')
# plt.ylabel('Signal Value / Relevance')

# # 创建虚拟的可映射对象
# cbar = plt.colorbar(cax, orientation='horizontal', label='Relevance Value')

# plt.tight_layout()
# plt.show()
