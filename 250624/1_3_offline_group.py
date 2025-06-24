import heapq

N, M, P = map(int, input().split()) # 정점 수, 간선 수, 목적지 idx
graph_a = [[] for _ in range(N+1)]  # 목적지로 가는 경우
graph_b = [[] for _ in range(N+1)]  # 목적지에서 돌아오는 경우

for _ in range(M):
    s, e, w = map(int, input().split())
    graph_a[e].append((w, s))
    graph_b[s].append((w, e))

dist_a = [float('inf')] * (N+1)
dist_b = [float('inf')] * (N+1)
dist_a[P] = 0
dist_b[P] = 0

# 목적지로 가는 경우
pq = [(0, P)]
while pq:
    w, n = heapq.heappop(pq)
    if w > dist_a[n]:
        continue
    for nw, nn in graph_a[n]:
        nw = w + nw
        if nw < dist_a[nn]:
            dist_a[nn] = nw
            heapq.heappush(pq, (nw, nn))
# 목적지에서 돌아오는 경우
pq = [(0, P)]
while pq:
    w, n = heapq.heappop(pq)
    if w > dist_b[n]:
        continue
    for nw, nn in graph_b[n]:
        nw = w + nw
        if nw < dist_b[nn]:
            dist_b[nn] = nw
            heapq.heappush(pq, (nw, nn))

max_dist = -1
for i in range(1, N+1):
    dist = dist_a[i]+dist_b[i]
    if max_dist < dist:
        max_dist = dist
print(max_dist)