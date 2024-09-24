import matplotlib.pyplot as plt
import numpy as np

def fancha_curve(x):
    return np.sin(5*np.pi*x) * np.exp(-x)

# 生成曲线数据
x = np.linspace(0, 2, 1000)
y = fancha_curve(x)

# 绘制曲线
plt.plot(x, y, color='black')

# 应用配色方案
colors = plt.cm.viridis(np.linspace(0, 1, len(x)))
for i in range(len(x)-1):
    plt.fill_betweenx([y[i], y[i+1]], [x[i], x[i+1]], color=colors[i])

# 设置标题和坐标轴标签
plt.title("繁花曲线")
plt.xlabel("X")
plt.ylabel("Y")

# 显示图形
plt.show()
