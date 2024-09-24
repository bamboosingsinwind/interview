N = int(input())
A = [int(x) for x in input().split()]
K = int(input())
LMm = [[int(x) for x in input().split()] for _ in range(K)]

from collections import defaultdict
a = [0] + A
nxs = defaultdict(list)
for line in LMm:
    nxs[line[0]] += line[2:]

def check(node,cnt,prods):
    if prods[node] >= cnt:
        prods[node] -= cnt
        return True
    cnt -= prods[node]
    prods[node] = 0
    if node not in nxs:return False #无法拼凑
    for nx in nxs[node]:
        if not check(nx,cnt,prods):return False
    return True
l,r = 0,10**6
while l<r:
    mid = (l+r+1)//2
    if check(N,mid,a):
        l = mid
    else:
        r = mid - 1
print(r)
        