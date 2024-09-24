amount = int(input())
price = list(map(int,input().split()))
res = []
def dfs(price,amount,line,cur):
    if cur >amount:
        return
    elif cur == amount:
        res.append(line)
        line = []
        return
    for i in price:
        line.append(i)
        cur += i
        dfs(price,amount,line,cur)
        line.pop()
        
dfs(price,amount,[],0)
print(res)
    