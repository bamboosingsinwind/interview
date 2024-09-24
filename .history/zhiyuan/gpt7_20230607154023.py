import numpy as np
import matplotlib.pyplot as plt

# 定义函数
def f(t):
    return np.exp(np.cos(t)) - 2 * np.cos(4 * t) + np.sin(t/12)**5

# 生成数据
t = np.linspace(0, 24 * np.pi, 1000)
y = f(t)

# 绘制图像
plt.plot(t, y)

# 设置标题和坐标轴标签
plt.title(r"$e^{\cos(t)} - 2\cos(4t) + \sin^{5}\left(\frac{t}{12}\right)$")
plt.xlabel("t")
plt.ylabel("y")

# 显示图像
plt.show()
