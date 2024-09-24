n = int(input())
xh = []
for _ in range(n):
    xh.append([int(i) for i in input().split()])

def solve(xh,n):
    if n < 3: return n
    res = 1
    for i in range(1,n-1):
        x_pre,x_next = xh[i-1][0],xh[i+1][0]
        x,h = xh[i]
        if x - h > x_pre:
            res += 1
        elif x + h < x_next:
            res += 1
            xh[i][0] = x + h
    res += 1
    return res
print(solve(xh,n))