import pprint
import sys
sys.stdin = open('input.txt', 'r')
from collections import deque


def bfs():
    while q:
        r, c, k = q.popleft()
        if r == R-1 and c == C-1:
            return visited[r][c] - 1

        for dr, dc in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            nr = r + dr
            nc = c + dc
            if 0 <= nr < R and 0 <= nc < C and arr[nr][nc] != 1 and not visited[nr][nc]:
                visited[nr][nc] = visited[r][c] + 1
                q.append((nr, nc, k))

        if k > 0:
            k -= 1
            for hr, hc in [[-2, 1], [-1, 2], [1, 2], [2, 1], [2, -1], [1, -2], [-1, -2], [-2, -1]]:
                hnr = r + hr
                hnc = c + hc              
                if 0 <= hnr < R and 0 <= hnc < C and arr[hnr][hnc] != 1 and not visited[hnr][hnc]:
                    visited[hnr][hnc] = visited[r][c] + 1
                    q.append((hnr, hnc, k))
        # print(q)
    return -1
        
K = int(input())
C, R = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(R)]
visited = [[0]*C for _ in range(R)]
visited[0][0] = 1
q = deque([(0, 0, K)])
print(bfs())
# pprint.pprint(visited, width=30)
# bfs()
