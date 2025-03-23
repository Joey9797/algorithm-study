import sys
sys.stdin = open("input.txt", "r")
import heapq
'''
dijkstra(?) + memoization 으로 품 ----------------------------------------------------------------
'''
dr, dc = [0, 1, 0, -1], [1, 0, -1, 0]
def dijkstra():
    while hq:
        w, r, c = heapq.heappop(hq)
        
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            if 0 <= nr < N and 0 <= nc < N:
                if memo[nr][nc] != -1:
                    continue
                memo[nr][nc] = memo[r][c] + map_info[nr][nc]
                if nr == N-1 and nc == N-1:
                    return memo[nr][nc]
                heapq.heappush(hq, (memo[nr][nc], nr, nc))
    


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    map_info = [[*map(int, input())] for _ in range(N)]
    hq = [(0, 0, 0)]
    memo = [[-1] * N for _ in range(N)]
    memo[0][0] = 0
    print(f"#{tc} {dijkstra()}")