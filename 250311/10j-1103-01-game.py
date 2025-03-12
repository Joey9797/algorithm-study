from collections import deque
import sys
sys.stdin = open("input.txt", "r")

'''
실패한 코드 ----------------------------------------------------------------
'''
N, M = [*map(int, input().split())]
board = [[int(c) if c.isdigit() else c for c in input()] for _ in range(N)]
stack = [(0, 0)]

is_infinite = False
cnt = 0
total = 0
while stack and is_infinite == False:
    sr, sc = stack.pop()
    step = board[sr][sc]
    cnt += 1

    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    for i in range(4):
        nr = sr + dr[i]*step
        nc = sc + dc[i]*step
        if 0 <= nr < N and 0 <= nc < M and board[nr][nc] != 'H':
            if board[nr][nc] >= N and board[nr][nc] >= M:
                continue
            if board[nr][nc] == step:
                result = -1
                is_infinite = True
                break
            stack.append((nr, nc))
        else:
            total = max(total, cnt)
            cnt -= 1
if is_infinite == False:
    result = total
print(result)