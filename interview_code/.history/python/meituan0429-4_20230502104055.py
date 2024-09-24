n,m,k = list(map(int,input().split()))
request = list(map(int,input().split()))
arrive = list(map(int,input().split()))

re_ar = [[i,j] for i,j in zip(request,arrive)]
re_ar = sorted(re_ar,key=lambda x:[x[1],x[0]])
#first
cur = re_ar[0][1]
res = 0#re_ar[0][0] - k
id = k#re_ar[0][0]
# cur += res*m
# re_ar.pop(0)
#cur re_ar res-->next()
def recursion(cur,id,res):
    if len(re_ar)==0:
        return res
    # global cur,res
    dis = 1e10
    next = 1e6
    for i in range(len(re_ar)):
        if cur >= re_ar[i][1]:
            if dis>abs(id-re_ar[i][0]) or (dis==abs(id-re_ar[i][0]) and id>re_ar[i][0]):
                dis = abs(id-re_ar[i][0])
                next = int(i)
                # id = re_ar[i][0] #注意id不能变，只有在循环完将next的磁道号赋给id 
        else:
            break
    id = re_ar[next][0]
    cur += dis*m
    res += dis
    re_ar.pop(next)
    return recursion(cur,id,res)
    
print(recursion(cur,id,res))
    
            
        
    