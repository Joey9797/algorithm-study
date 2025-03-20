import sys
sys.stdin = open("input.txt", "r")
from collections import deque


dr, dc = [0, 1, 1, 1, 0, -1, -1, -1], [1, 1, 0, -1, -1, -1, 0, 1]
W, H = map(int, input().split())
while W != 0 and H != 0:
    visited = [[0]*W for _ in range(H)]
    cnt = 0
    arr = [[*map(int, input().split())] for _ in range(H)]
    for r in range(H):
        for c in range(W):
            no_way = False
            q = deque()
            if visited[r][c]:
                continue
            if arr[r][c] == 0:
                continue
            q.append((r, c))
            visited[r][c] = 1
            cnt += 1

            while q:
                sr, sc = q.popleft()
                for i in range(8):
                    nr = sr + dr[i]
                    nc = sc + dc[i]
                    if 0 <= nr < H and 0 <= nc < W and not visited[nr][nc] and arr[nr][nc] == 1:
                        visited[nr][nc] = 1
                        q.append((nr, nc))
                        
    print(cnt)
    W, H = map(int, input().split())
    