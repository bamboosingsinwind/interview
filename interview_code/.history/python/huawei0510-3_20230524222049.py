m = int(input())
n = int(input())
from collections import defaultdict
# map = defaultdict([])
# for _ in range(n):
#     a,b,c = map(int,input().split())
#     map[a].append([b,c])
map = [[int("inf") for _ in range(m+1)] for _ in range(m+1)]
for _ in range(n):
    a,b,c = map(int,input().split())
    map[a][b] = c
    
src = int(input())
def dijkstra(map,src):
    
    