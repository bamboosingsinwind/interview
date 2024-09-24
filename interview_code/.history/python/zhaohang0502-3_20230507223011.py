N = int(input())
A = [int(x) for x in input().split()]
K = int(input())
LMm = [[int(x) for x in input().split()] for _ in range(K)]

from collections import defaultdict
from typing import List
a = [0] + A
nxs = defaultdict(list)
for line in LMm:
    nxs[line[0]] += line[2:]

# def check(node:int,cnt:int,prods:List[int]):
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
    mid = (l+r+1)>>1
    # print(list(a))
    if check(N,mid,list(a)):#这里加了list，每次调用完不改变a;  如果是check(N,mid,a)，相当于a为全局变量，会改变a的内容

        l = mid
    else:
        r = mid - 1
print(r)
        