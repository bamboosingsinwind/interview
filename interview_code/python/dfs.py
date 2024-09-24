A = list(range(4))
cur = [-1]*7
#A中n个值，依次（从左到右顺序不变）赋给长度为N的cur中n个值
def dfs(index,i,n,N,cur):
    if i==n:
        print(cur)
        return
    for j in range(index,N):
        cur[j] = A[i]
        dfs(j+1,i+1,n,N,cur) #j+1保证j的上三角遍历，i+1保证对A遍历    
        cur[j] = -1 #回溯
dfs(0,0,4,7,cur)