import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-2, 2, 100)
y = x ** 2 - 1

plt.plot(x, y)
plt.show()