import time
t0 = time.time()
days = [list(map(int, input().split())) for _ in range(7)]
allow = [list(set(range(10))-set(day[1:])) for day in days]
inf = False
res = 1000
def dfs(i,chioce):
    if i == 7:
        if(len(chioce)>0):#1-7天，走通的方案
            global res
            res = min(res,len(chioce))#维护每种走通方案的最小值
        return 
    for cur in allow[i]:
        if cur not in chioce:
            chioce.add(cur)
            dfs(i+1,chioce)
            chioce.remove(cur)#回溯
        else:
            dfs(i+1,chioce)
dfs(0,set())                 
if inf:
    print(-1)
else:
    print(res)
print(time.time()-t0)       
                 
    
        