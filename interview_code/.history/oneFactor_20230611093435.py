#%%
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
# %%
close = pd.read_csv("close.csv", index_col=0)
print(close.shape)
print(close.index)
print(close.columns)
# %%
