li = [[0,0,1,1],[4,4,2,2]]
def area(li):#1:white, -1:black
    map = [[1 for i in range(100)] for _ in range(100)]
    #千万不能[[1]*100]*100初始化，否则改变一个其他跟着改变
    cnt = 0
    for i in li:
        l,r = min(i[0],i[2]),max(i[0],i[2])
        u,d = min(i[1],i[3]),max(i[1],i[3])
        print(l,r,u,d)
        for j in range(l,r):
            for k in range(u,d):
                cnt += 1
                map[j][k] *= -1#map[j][k]
    res = 0
    for row in map:
        res += row.count(1)
    return res
print(area(li))
    