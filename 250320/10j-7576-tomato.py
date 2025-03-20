from collections import deque


def bfs():
    dr, dc = [0, 1, 0, -1], [1, 0, -1, 0]
    q = deque()
    for r in range(N):
        for c in range(M):
            never_cnt = 0
            for i in range(4):
                nr = r + dr[i]
                nc = c + dc[i]
                if 0 > nr or nr >= N or 0 > nc or nc >= N:
                    if tomato[r][c] == 0 and tomato[nr][nc] == -1:
                        never_cnt += 1




M, N = int(input())
tomato = [[*map(int, input().split())] for _ in range(N)]

