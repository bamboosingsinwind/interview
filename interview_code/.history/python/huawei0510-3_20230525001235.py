m = int(input())
n = int(input())
from collections import defaultdict
import numpy as np
# map = defaultdict([])
# for _ in range(n):
#     a,b,c = map(int,input().split())
#     map[a].append([b,c])
map = [[np.inf for _ in range(m+1)] for _ in range(m+1)]
for i in range(1,m+1):
    map[i][i] = 0
for _ in range(n):
    a,b,c = [int(i) for i in input().split(" ")]#map(int,input().split())
    map[a][b] = c
    
src = int(input())
def dijkstra(map,src):
    book = {src}
    remain = set(range(1,m+1)) - book
    while True:
        id,dis = -1,np.inf
        # for b in book:
        b = src
        for r in remain:
            if map[b][r] + map[r][r] < dis:
                dis = map[b][r] + map[r][r]
                id = r
        if id == -1:
            li = [i for i in map[src][1:] if i != np.inf]
            return len(li),max(li)
        book.add(id)
        remain.remove(id)
        for i in remain:
            if map[src][id] + map[id][id] + map[id][i] + map[i][i] < map[src][i]:
                map[src][i] = map[src][id] + map[id][id] + map[id][i] + map[i][i]
  
print(dijkstra(map,src))           
            
    
        
    
    
    
    
    
    