import pandas as pd
from datetime import datetime
import time 
df = pd.read_excel("C:\\Users\\26284\\Desktop\\zjq\\加班\\考勤.xlsx")
# print(df)
df["week"] = df["日期"].dt.dayofweek
def time_diff(st,end):
    t1 = datetime.strptime(st, "%H:%M:%S") 	# 将日期格式化为格式化成YYYY-MM-DD格式
    t2 = datetime.strptime(end, "%H:%M:%S") 	# 将日期格式化为格式化成YYYY-MM-DD格式