N,K = map(int,input().split())
cate = list(map(int,input().split()))
S = [input() for _ in range(K)]

import heapq
from collections import defaultdict
from math import inf

id2cate = [i-1 for i in cate]
cate2id = defaultdict(list)
for i in range(N):
    cate2id[id2cate[i]].append(i)

def dijstra():
    dis = [inf] * N
    dis[0] = 0
    q = [(0,0)]
    while q:
        d,id = heapq.heappop(q) # node is a tuple (dist, index)
        if id == N-1:return d  # return distance to the last node
        if dis[id] < d: continue # ignore the same node or not considered.
        for j in range(K):
            if S[id2cate[id]][j] == '1':
                for idd in cate2id[j]:
                    curDis = d + abs(id - idd)
                    if curDis < dis[idd]:# distance(#0-id--idd)<distance(0--idd)
                        dis[idd] = curDis 	# update the distance.
                        heapq.heappush(q, (curDis, idd)) # add the new distance.
    return -1 # failure, no solution found.
print(dijstra())
