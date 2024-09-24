days = [list(map(int, input().split())) for _ in range(7)]
allow = [list(set(range(10))-set(day[1:])) for day in days]
inf = False

def dfs(i,chioce):
    if i == 7:
        return len(chioce)
    for cur in allow[i]:
        if cur not in chioce:
            chioce.add(cur)
            dfs(i+1,chioce)
            chioce.remove(cur)#回溯
        else:
            dfs(i+1,chioce)
                  
if inf:
    print(-1)
else:
    print(dfs(0,set()))
        
                 
    
        