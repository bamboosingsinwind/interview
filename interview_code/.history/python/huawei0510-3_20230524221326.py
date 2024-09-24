m = int(input())
n = int(input())
from collections import defaultdict
map = defaultdict([])
for _ in range(n):
    a,b,c = map(int,input().split())
    map[a].append([b,c])
src = int(input())
def dijkstra(map,src):
    P = [0,0] + [int("inf") for _ in range(m-1)]
    se
    