from math import inf
#邻接表版======================
import heapq
from collections import defaultdict
nxs = defaultdict(list)
##input
n = int(input())
for _ in range(n):#n: num of nodes
    u,v,w = [int(x) for x in input().split()]#u: source, v: destination, w: weight e.g
    nxs[u].append((v,w))# unidirectional
    # nxs[v].append((u,w))# bi-directional
def dij(nxs,src,dst):
    dis = [inf for _ in range(n+1)]
    dis[src] = 0
    q = [(0,src)] # (dis,node)
    while q:
        d,node = heapq.heappop(q)
        if node == dst:
            return d
        for nx,nxdis in nxs[node]:
            curdis = d + nxdis
            if curdis < dis[nx]:
                dis[nx] = curdis
                heapq.heappush(q, (curdis, nx))

#邻矩阵版======================
map = [[inf for _ in range(n+1)] for _ in range(n+1)]
for i in range(1,n+1):
    map[i][i] = 0
for _ in range(n):
    u,v,w = [int(i) for i in input().split(" ")]#map(int,input().split())
    map[u][v] = w

def dijkstra(map,src,dst):
    q = [(0,src)] # (dis,node)
    while q:
        d,node = heapq.heappop(q)
        if node == dst:
            return d
        for nx,nxdis in nxs[node]:
            curdis = d + nxdis
            if curdis < dis[nx]:
                dis[nx] = curdis
                heapq.heappush(q, (curdis, nx))
    
    