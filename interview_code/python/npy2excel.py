import numpy as np
import pandas as pd

data = np.load("D:\\seadrive\\data\\朱向前\\我的资料库\\阜外项目\\result0816\\code\\mygroup_new70label.npy", allow_pickle=True)
df = pd.DataFrame(data)
df.to_excel("D:\\seadrive\\data\\朱向前\\我的资料库\\阜外项目\\result0816\\code\\mygroup_new70label.xlsx")