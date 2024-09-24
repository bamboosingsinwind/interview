amount = int(input())
price = eval(input())
res = []
from copy import deepcopy
def dfs(price,amount,line,cur):
    if cur > amount:
        return
    elif cur == amount:
        line_cp = deepcopy(line)
        res.append(line_cp)
        # line = []
        return
    for i in price:
        line.append(i)
        cur += i
        dfs(price,amount,line,cur)
        line.pop()
        
dfs(price,amount,[],0)
print(res)
    