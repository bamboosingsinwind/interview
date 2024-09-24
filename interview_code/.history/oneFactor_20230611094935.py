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
r0 = close / close.shift(1)
print(r0)
# %%
factor1 = r0.rolling(window=10).mean()  
# %%
print(r0.head(20)) 
print(factor1.head(10)) 