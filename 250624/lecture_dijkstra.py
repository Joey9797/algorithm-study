import heapq
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [[*map(int, input().split())] for _ in range(N)]
dr, dc = [0, 1, 0, -1], [1, 0, -1, 0]
pq = []
dist = [[float('inf')] * M for _ in range(N)]
heapq.heappush(pq, (arr[0][0], 0, 0))
dist[0][0] = arr[0][0]

while pq:
    w, r, c = heapq.heappop(pq)
    if w > dist[r][c]:
        continue

    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if 0 <= nr < N and 0 <= nc < M:
            nw = w + arr[nr][nc]
            if nw < dist[nr][nc]:
                dist[nr][nc] = nw
                heapq.heappush(pq, (nw, nr, nc))

print(dist[N-1][M-1])
