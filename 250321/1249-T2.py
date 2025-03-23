import sys
sys.stdin = open("input.txt", "r")
import heapq

dr, dc = [0, 1, 0, -1], [1, 0, -1, 0]
def dijkstra(w, sr, sc):
    if sr == N-1 and sc == N-1:
        return 
    
    while hq:
        w, r, c = heapq.heappop(hq)
        
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            if 0 <= nr < N and 0 <= nc < N:
                if w + map_info[nr][nc] > memo[nr][nc]:
                    continue
                w += map_info[nr][nc]
                heapq.heappush(hq, (w, nr, nc))
                dijkstra(w, nr, nc)
    return
    


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    map_info = [[*map(int, input())] for _ in range(N)]
    hq = [(0, 0, 0)]
    # memo = [[-1] * N for _ in range(N)]
    print(dijkstra(0, 0, 0))