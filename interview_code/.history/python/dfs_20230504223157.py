A = [1]*4
cur = [0]*7
def dfs(index,i,n,N,cur):
    if i==n:
        print(cur)
        return
    for j in range(index,N):
        # print(i,j)
        cur[j] = A[i]
        dfs(j+1,i+1,n,N,cur)     
        cur[j] = 0
dfs(0,0,4,7)