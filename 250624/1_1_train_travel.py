import heapq

N, T = map(int, input().split())
graph = [[] for _ in range(N)]
for _ in range(T):
    s, e, w = map(int, input().split())
    graph[s].append((w, e))

def dijkstra(sn):
    pq = [(0, sn)]
    dist = [float('inf')] * N
    dist[sn] = 0

    while pq:
        w, n = heapq.heappop(pq)
        if w > dist[n]:
            continue

        for nw, nn in graph[n]:
            new_w = w + nw
            if new_w < dist[nn]:
                dist[nn] = new_w
                heapq.heappush(pq, (new_w, nn))
    
    if dist[N-1] == float('inf'):
        return 'impossible'
    return dist[N-1]

print(dijkstra(0))