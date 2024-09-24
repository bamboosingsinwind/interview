import heapq

n, m, h = map(int, input().split())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    u, v, w, d = map(int, input().split())
    graph[u].append((v, w, d))
    graph[v].append((u, w, d))

def dijkstra(weight):
    dist = [float('inf')] * (n+1)
    dist[1] = 0
    
    heap = [(0, 1)]
    
    while heap:
        d, u = heapq.heappop(heap)
        
        if dist[u] < d:
            continue
        
        for v, w, d in graph[u]:
            if w >= weight:
                alt = dist[u] + d
                if alt < dist[v]:
                    dist[v] = alt
                    heapq.heappush(heap, (alt, v))
    
    return dist[n]

lo, hi = 0, float('inf')

while lo < hi:
    mid = (lo + hi + 1) // 2
    if dijkstra(mid) <= h:
        lo = mid
    else:
        hi = mid - 1

print(lo)