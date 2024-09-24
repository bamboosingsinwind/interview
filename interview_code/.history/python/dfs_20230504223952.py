A = [1]*4
cur = [0]*7
def dfs(index,i,n,N,cur):#
    if i==n:
        print(cur)
        return
    for j in range(index,N):
        cur[j] = A[i]
        dfs(j+1,i+1,n,N,cur) #j+1保证j的上三角遍历，i+1保证对A遍历    
        cur[j] = 0 #回溯
dfs(0,0,4,7,cur)