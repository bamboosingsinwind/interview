li = [[0,0,1,1],[4,4,2,2]]
def area(li):#1:white, -1:black
    map = [[1]*100]*100
    cnt = 0
    for i in li:
        l,r = min(i[0],i[2]),max(i[0],i[2])
        u,d = min(i[1],i[3]),max(i[1],i[3])
        print(l,r,u,d)
        for j in range(l,r):
            for k in range(u,d):
                cnt += 1
                map[j][k] = -map[j][k]
    res = 0
    for i in map:
        res += i.count(1)
    print("cnt",cnt)
    return res
print(area(li))
    