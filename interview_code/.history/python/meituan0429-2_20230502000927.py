import time
t0 = time.time()
days = [list(map(int, input().split())) for _ in range(7)]
allow = [list(set(range(10))-set(day[1:])) for day in days]
inf = False

def fun(num,allow):
    if(len(allow)==0):
        return num
    num += 1
    cnt = [0] * 10
    for al in allow:
        if(len(al)==0):
            global inf
            inf = True
            allow.remove(al)
        for a in al:
            cnt[a] += 1
    id = cnt.index(max(cnt))  
 
    for al in range(len(allow)-1,-1,-1):#倒序遍历，for al in allow: remove不可行，因为删除后会跳过下一个
        if id in allow[al]:
            allow.pop(al)
    return fun(num,allow)
if inf:
    print(-1)
else:
    print(fun(0,allow))
print(time.time-t0)      
                 
    
        