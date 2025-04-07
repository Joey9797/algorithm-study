import pprint
import sys
# sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
from collections import deque


def bfs():
    while q:
        r, c, k = q.popleft()

        if r == R-1 and c == C-1:
            return visited[r][c][k] - 1

        for dr, dc in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            nr = r + dr
            nc = c + dc
            if 0 <= nr < R and 0 <= nc < C and arr[nr][nc] != 1 and not visited[nr][nc][k]:
                visited[nr][nc][k] = visited[r][c][k] + 1
                q.append((nr, nc, k))

        if k > 0:
            for hr, hc in [[-2, 1], [-1, 2], [1, 2], [2, 1], [2, -1], [1, -2], [-1, -2], [-2, -1]]:
                hnr = r + hr
                hnc = c + hc              
                if 0 <= hnr < R and 0 <= hnc < C and arr[hnr][hnc] != 1 and not visited[hnr][hnc][k-1]:
                    visited[hnr][hnc][k-1] = visited[r][c][k] + 1
                    q.append((hnr, hnc, k-1))
        # print(q)
    return -1
        
K = int(input()) # K = 말처럼 점프할 수 있는 횟수
C, R = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(R)]
''' 
visited는 3차원 배열 형태여야 한다.
왜냐하면 K가 0번 남은 것과, K가 1번 남은 것은 다른 경우인데,
해당 지점에 방문한 순간에 visited를 처리해버리면, K가 다른 경우를 고려할 수 없기 때문이다.
즉, 말이 이동할 수 있는 횟수(k)가 바뀔 수 있기 때문에,
각기 다른 k 상태마다 "판 전체(visited)를 따로 들고 다닌다고 생각하면 편하다.

visited = [
    [  # row 0
        [0, 0, 0],  # col 0 → k=0~2
        [0, 0, 0],  # col 1
        [0, 0, 0]   # col 2
    ],
    [  # row 1
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ],
    ...
]
'''
visited = [[[0]*(K+1) for _ in range(C)] for _ in range(R)]
visited[0][0][K] = 1
q = deque([(0, 0, K)])
print(bfs())
# pprint.pprint(visited, width=30)
# bfs()
