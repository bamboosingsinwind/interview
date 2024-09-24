li = [[0,0,1,1],[4,4,2,2]]
def area(li):#1:white, -1:black
    map = [[1]*10]*10
    for i in li:
        l,r = min(i[0],i[2]),max(i[0],i[2])
        u,d = min(i[1],i[3]),max(i[1],i[3])
        for j in range(l,r):
            for k in range(u,d):
                map[j][k] = -map[j][k]
    res = 0
    for i in map:
        res += i.count(1)
    return res
print(area(li))
    