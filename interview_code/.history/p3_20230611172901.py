import pandas as pd
import numpy as np

factor1 = pd.read_excel("factor1-cp.xlsx")

# 去极值
lower_bound = factor1.quantile(0.25, axis=1)  # 每个横截面的下界，2%分位数
upper_bound = factor1.quantile(0.75, axis=1)  # 每个横截面的上界，98%分位数
factor1 = np.where(factor1 > upper_bound.to_numpy()[:, np.newaxis], upper_bound.to_numpy()[:, np.newaxis], factor1)  # 超过上界的赋值为上界
factor1 = np.where(factor1 < lower_bound.to_numpy()[:, np.newaxis], lower_bound.to_numpy()[:, np.newaxis], factor1)  # 低于下界的赋值为下界

# 标准化
factor1_mean = factor1.mean(axis=1)  # 每个横截面的均值
factor1_std = factor1.std(axis=1)  # 每个横截面的标准差
factor1 = (factor1 - factor1_mean[:, np.newaxis]) / factor1_std[:, np.newaxis]  # 标准化

# 创建处理后的因子矩阵
# factor = pd.DataFrame(factor1, index=close.index, columns=close.columns)

# 打印结果
# print(factor)