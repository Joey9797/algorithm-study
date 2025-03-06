T = int(input())
for tc in range(1, T+1):
    N = int(input())
    tri = [[1]] + [[1, 1]] + [[0]*i for i in range(3, N+1)]
    for i in range(2, N):
        for j in range(i+1):
            if j == 0 or j == i:
                tri[i][j] = 1
            else:
                tri[i][j] = tri[i-1][j-1] + tri[i-1][j]

    print(f'#{tc}')
    for i in range(N):
        print(' '.join(map(str, tri[i])))