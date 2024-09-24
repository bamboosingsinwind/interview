n,m,q = map(int,input().split())
str = ",".join(range(1,n*m//2+1))
M = []
for i in range(n):
    M.append(str[i*m,(i+1)*m])
for _ in range(q):
    x1,y1,x2,y2 = map(int,input().split())  
    cnt = 0
    for i in range(x1,x2+1):
        cnt += list(M[i][y1:y2+1]).count(',')
    print(cnt)
    