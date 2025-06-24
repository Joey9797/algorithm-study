import heapq

dr, dc = [0, 1, 0, -1], [1, 0, -1, 0]
sr, sc = map(int, input().split())
N = int(input())
arr = [[*map(int, input().split())] for _ in range(N)]
dist = [[float('inf')] * N for _ in range(N)]

dist[sr][sc] = arr[sr][sc]
pq = [(arr[sr][sc], sr, sc)]

while pq:
    w, r, c = heapq.heappop(pq)
    if w > dist[r][c]:
        continue
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if 0 <= nr < N and 0 <= nc < N and arr[nr][nc] != -1:
            nw = w + arr[nr][nc]
            if nw < dist[nr][nc]:
                dist[nr][nc] = nw
                heapq.heappush(pq, (nw, nr, nc))

max_dist = -1
for r in range(N):
    for c in range(N):
        if dist[r][c] == float('inf'):
            continue
        if dist[r][c] > max_dist:
            max_dist = dist[r][c]
            
print(max_dist)
