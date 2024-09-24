#%%
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
# %%
close = pd.read_csv("close.csv", index_col=0)
print(close.shape)
print(close.index)
print(close.columns)
# %% Problem 1
r = close.shift(-5) / close - 1
r0 = close / close.shift(1) - 1
print(r0)
# %%
factor1 = r0.rolling(window=10,min_periods=1).mean()  
# %%
factor2 = r0.apply(lambda x: x.rank(ascending=False,na_option='keep') / x.count(), axis=1)
print(factor2)
factor2.to_csv("factor2.csv")  
# %%
factor3 = r0.rolling(10, min_periods=1).apply(lambda x: pd.Series(x).rank(na_option='keep').iloc[-1] / x.count())
print(factor3)
# %%
weights = np.arange(1, 0, -0.1)  # 权重数组 [1, 0.9, ..., 0.1]
factor4 = r0.rolling(10, min_periods=1).apply(lambda x: np.sum(x.fillna(0) * weights[:x.shape[0]]))
print(factor4)
# %%
factors = { "factor1": factor1, "factor2": factor2, "factor3": factor3, "factor4": factor4,}
for name, factor in factors.items():
    factor.to_csv(f"{name}.csv")
    print(f"{name}: coverage={factor.count().mean() / factor.shape[0]}")  
# %%
r0.to_csv("r0.csv")
# %%
