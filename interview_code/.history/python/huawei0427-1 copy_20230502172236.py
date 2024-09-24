N = int(input())
records = list(input() for _ in range(N))
records_id = {}#这里必须用字典
res = []
for i,line in enumerate(records):
    no,time,dis,device,reg = line.split(',')
    time,dis = int(time),int(dis) 
    if no not in records_id:#按照no归类
        records_id[no] = []
    records_id[no].append([time,dis,device,reg,i])
    if device != reg:
        res.append(i)
for id in records_id:
    for i in range(len(records_id)-1):
        time1,dis1,id1 = records_id[id][i][0],records_id[id][i][1],records_id[id][i][-1]
        for j in range(i,len(records_id)):
            time2,dis2,id2 = records_id[id][j][0],records_id[id][j][1],records_id[id][j][-1]
            if abs(time1-time2)<=60 and abs(dis1-dis2)>5:
                res += [id1,id2]
if len(res) == 0:
    print("null")       
else:
    res = sorted(list(set(res)))
    res_record = [records[i] for i in res]
    print(";".join(res_record))
    