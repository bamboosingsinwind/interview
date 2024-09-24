import pandas as pd
from datetime import datetime
import time 
df = pd.read_excel("C:\\Users\\26284\\Desktop\\zjq\\加班\\work_time.xlsx")
# print(df)

def time_diff(st,end):
    t1 = datetime.strptime(st, "%H:%M:%S") 	# 将日期格式化为格式化成YYYY-MM-DD格式
    t2 = datetime.strptime(end, "%H:%M:%S") 	# 将日期格式化为格式化成YYYY-MM-DD格式
    return (t2 - t1).total_seconds()/3600
df["(下班-上班班)|小时"] = df.apply(lambda x: time_diff(x['上班时间'],x['下班时间']),axis=1)
df["(下班-9点)|小时"] = df.apply(lambda x: time_diff("9:00:00",x['下班时间']),axis=1)
df["week"] = df["日期"].dt.dayofweek