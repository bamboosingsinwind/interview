import pandas as pd
from datetime import datetime
import time 
from chinese_calendar import is_holiday,is_workday
df = pd.read_excel("C:\\Users\\26284\\Desktop\\zjq\\加班\\work_time.xlsx")
# print(df)

def time_diff(st,end):
    # return (end - st).total_seconds()/3600
    t1 = datetime.strptime(str(st), "%H:%M:%S") 	# 将日期格式化为格式化成YYYY-MM-DD格式
    t2 = datetime.strptime(str(end), "%H:%M:%S") 	# 将日期格式化为格式化成YYYY-MM-DD格式
    return (t2 - t1).total_seconds()/3600
def weight(time):
    # time = datetime.strptime(time, "%Y-%m-%d")
    if is_holiday(time): 	# 判断是否周末或晚于21:00
        return 3
    elif is_workday(time):
        return 1.5
    else:
        return 2

df["(下班-上班)|小时"] = df.apply(lambda x: time_diff(x['上班时间'],x['下班时间']),axis=1)
df["(下班-9点)|小时"] = df.apply(lambda x: time_diff("9:00:00",x['下班时间']),axis=1)
df["星期"] = df["日期"].dt.dayofweek + 1
df["加班费权重系数"] = df.apply(lambda x:weight(x["日期"]),axis = 1)
print(df)
df.to_excel("C:\\Users\\26284\\Desktop\\zjq\\加班\\work_time_processed.xlsx")