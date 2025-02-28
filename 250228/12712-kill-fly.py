'''
2
5 2
1 3 3 6 7
8 13 9 12 8
4 16 11 12 6
2 4 1 23 2
9 13 4 7 3
6 3
29 21 26 9 5 8
21 19 8 0 21 19
9 24 2 11 4 24
19 29 1 0 21 19
10 29 6 18 4 3
29 11 15 3 3 29'''
T = int(input())
for tc in range(1, T+1):
    N, M = list(map(int, input().split())) # 배열크기N, 분사되는 칸M
    fly = [list(map(int, input().split())) for _ in range(N)]
    max_dead = 0
    for r in range(N):
        for c in range(N):
            cnt1 = fly[r][c]
            for dr, dc in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
                for j in range(1, M):
                    nr = r + dr*j
                    nc = c + dc*j
                    if 0 <= nr < N and 0 <= nc < N:
                        cnt1 += fly[nr][nc]
            cnt2 = fly[r][c]
            for dr, dc in [[-1, 1], [1, 1], [1, -1], [-1, -1]]:
                for j in range(1, M):
                    nr = r + dr*j
                    nc = c + dc*j
                    if 0 <= nr < N and 0 <= nc < N:
                        cnt2 += fly[nr][nc]
            result = max(cnt1, cnt2)
            if max_dead < result:
                max_dead = result
    print(f"#{tc} {max_dead}")
