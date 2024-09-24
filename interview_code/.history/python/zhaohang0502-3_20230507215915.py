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
    if prods[node] == cnt:
        return True
    
        