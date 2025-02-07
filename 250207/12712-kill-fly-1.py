import pprint
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
29 11 15 3 3 29
'''
T = int(input())
for tc in range(1, T+1):
    N, M = list(map(int, input().split()))
    arr = [list(map(int, input().split())) for _ in range(N)]

    max_v = 0
    for i in range(N):
        for j in range(N):
            s1 = arr[i][j]
            s2 = arr[i][j]
            for di, dj in [[0, 1], [-1, 0], [0, -1], [1, 0]]:
                for m in range(1, M):
                    ni = i + di*m
                    nj = j + dj*m
                    if 0 <= ni < N and 0 <= nj < N:
                        s1 += arr[ni][nj]
            for di, dj in [[-1, -1], [-1, 1], [1, 1], [1, -1]]:
                for m in range(1, M):
                    ni = i + di * m
                    nj = j + dj * m
                    if 0 <= ni < N and 0 <= nj < N:
                        s2 += arr[ni][nj]
            if s1 > max_v:
                max_v = s1
            if s2 > max_v:
                max_v = s2
    print(f'#{tc} {max_v}')