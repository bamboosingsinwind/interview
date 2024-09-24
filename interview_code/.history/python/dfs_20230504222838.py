def dfs(index,i,n,N):
    if i==n:
        return
    for j in range(index,N):
        print(i,j)
        dfs(j+1,i+1,n,N)        #recursion ends once index+1 reaches the end of the array.
dfs(0,0,4,7)