T = 10
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    # 1=아래로 이동 2=위로 이동
    cnt = 0
    for r in range(N):
        for c in range(N):
            if r+1 < N and arr[r][c] == 1 and arr[r+1][c] == 0:
                arr[r][c], arr[r+1][c] = arr[r+1][c], arr[r][c]
            elif r+1 < N and arr[r][c] == 1 and arr[r+1][c] == 1:
                continue
            elif r+1 < N and arr[r][c] == 1 and arr[r+1][c] == 2:
                cnt += 1
                continue
    print(f'#{tc} {cnt}')
