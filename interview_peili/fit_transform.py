import numpy as np
from sklearn.preprocessing import StandardScaler

a = np.arange(4).reshape(2, 2)
print('标准化前:\n', a)
print('a.shape:', a.shape)

scaler = StandardScaler()

b_reshape = scaler.fit_transform(a.reshape(-1, 1)).reshape(2, 2)
print('通过fit_transform标准化后的：\n', b_reshape)
print(a)