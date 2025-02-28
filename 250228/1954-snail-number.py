import pprint


T = int(input())
N = int(input())
arr = [[0]*N for _ in range(N)]

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
d = 0
num = 1
arr[0][0] = 1
sr, sc = 0, 0
while num < N**2:
    nr = sr + dr[d]
    nc = sc + dc[d]
    if 0 <= nr < N and 0 <= nc < N and arr[nr][nc] == 0:
        num += 1
        sr, sc = nr, nc
        arr[sr][sc] = num
        
    else:
        d = (d+1) % 4
pprint.pprint(arr, width=30)