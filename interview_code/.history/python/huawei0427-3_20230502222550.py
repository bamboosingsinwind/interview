amount = int(input())
price = eval(input())
res = []
from copy import deepcopy
def dfs(price,amount,line,cur):
    if cur > amount:
        return
    elif cur == amount:
        line_cp = deepcopy(line)#必须用deepcopy,否则后续会改变
        res.append(line_cp)
        # line = []
        return
    for i in price:
        # line.append(i)
        # cur += i
        # dfs(price,amount,line,cur)
        # line.pop()
        # cur -= i
        dfs(price,amount,line+[i],cur+i)
        
dfs(price,amount,[],0)
print(res)
    