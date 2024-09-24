N = int(input())
record = [[input(),i] for i in range(N)]
record_sort = sorted(record,key=lambda x:x[0].split(',')[0])
clock_ori_dic = {}
for re in record_sort:
    id = re[0].split(",")[0]
    if id not in clock_ori_dic:
        clock_ori_dic[id] = []
    clock_ori_dic[id].append(re)  

res = []
def fun(clock_ori):
    # clock_ori = [input() for _ in range(N)]
    clock = [list(inp[0].split(","))+inp[1] for inp in clock_ori]
    N = len(clock)
    for i in range(N):
        if clock[i][3] != clock[i][4]:
            res.append(clock[i][-1])
        for j in range(1,3):
            clock[i][j] = int(clock[i][j])
    for i in range(N-1):
        for j in range(i,N):
            if abs(clock[i][1]-clock[j][1])<=60 and abs(clock[i][2]-clock[j][2])>5: 
                res += [clock[i][-1],clock[j][-1]]
for id in clock_ori_dic:
    fun(clock_ori_dic[id])    
res = sorted(list(set(res)))
if len(res)==0:
    print("null")
else:
    ans = [record[i][0] for i in res]
    ans = ";".join(ans)
    print(ans)
    