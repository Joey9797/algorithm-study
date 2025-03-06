T = int(input())
for tc in range(1, T+1):
    N = int(input())
    farm = [list(map(int, input())) for _ in range(N)]
    m = N//2
    cnt = 0
    for r in range(N):
        if r <= m:
            for c in range(m-r, m+r+1):
                cnt += farm[r][c]
        if r > m:
            for c in range(m-(N-r-1), m+(N-r)):
                cnt += farm[r][c]
    print(f"#{tc} {cnt}")