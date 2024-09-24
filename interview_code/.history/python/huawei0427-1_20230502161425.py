N = int(input())
clock = [list(input().split(",")) for _ in range(N)]
res = []
for i in range(N):
    if clock[i][3] != clock[i][4]:
        res.append(i)
    for j in range(1,3):
        clock[i][j] = int(clock[i][j])
for i in range(N-1):
    for j in range(i,N):
        if abs(clock[i][1]-clock[j][1])<=60 and abs(clock[i][2]-clock[j][2])>5: 
            res += [i,j]
res = sorted(list(set(res)))
for i in res:
    print(clock[i])