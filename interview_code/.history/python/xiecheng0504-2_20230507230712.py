n = int(input())
sa = [list(map(int,input.split())) for _ in range(n)]
sa = sorted(sa, key=lambda x: x[1],reverse=True)
res = -1
 
for i in range(1,n):
    for j in range(i-1):
        if sa[i][1] + sa[j][1] >= res and (sa[i][0] in sa[j][0] or sa[j][0] in sa[i][0]):
            res = sa[i][1] + sa[j][1]
            break
print(res)