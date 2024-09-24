import numpy as np
import matplotlib.pyplot as plt

def spiro_flower_curve(t):
    r = 0.8 + 0.2 * np.sin(7 * t)
    x = r * np.cos(t)
    y = r * np.sin(t)
    return x, y

# 生成数据
t = np.linspace(0, 2 * np.pi, 1000)
x, y = spiro_flower_curve(t)

# 绘制图像
plt.plot(x, y)

# 设置标题和坐标轴标签
plt.title("Spiro Flower Curve")
plt.xlabel("X")
plt.ylabel("Y")

# 显示图像
plt.show()
