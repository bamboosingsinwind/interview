days = list(map(int, input().split()) for _ in range(7))
allow = [list(set(range(10))-set(day)) for day in days]
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
    id = cnt.index(max(cnt))  # 找到最大的数字 ~~是python的一个特殊函数
    for al in allow:
        if id in al:
            allow.remove(al)
    return fun(num,allow)
if inf:
    print(-1)
else:
    print(fun(0,allow))
        
                 
    
        