T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    a_90 = [[0]*N for _ in range(N)]
    a_180 = [[0]*N for _ in range(N)]
    a_270 = [[0]*N for _ in range(N)]

    for r in range(N):
        for c in range(N):
            a_90[r][c] = arr[N-c-1][r]
            a_180[r][c] = arr[N - r - 1][N - c - 1]
            a_270[r][c] = arr[c][N - r - 1]

    print(f'#{tc}')
    for i in range(N):
        print(''.join(list(map(str, a_90[i]))), ''.join(list(map(str, a_180[i]))), ''.join(list(map(str, a_270[i]))))
