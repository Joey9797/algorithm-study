import sys
sys.stdin = open("input.txt", "r")

def dfs(sr, sc, sum_v):
    global total
    
    if sr == N-1 and sc == N-1:
        total = min(sum_v, total)
        return
    
    for dr, dc in [(0, 1), (1, 0)]:
        nr = sr + dr
        nc = sc + dc
        if 0 <= nr < N and 0 <= nc < N:
            dfs(nr, nc, sum_v+arr[nr][nc])

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [[*map(int, input().split())] for _ in range(N)]
    total = 1700
    dfs(0, 0, arr[0][0])
    print(f"#{tc} {total}")