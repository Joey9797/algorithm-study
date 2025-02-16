for tc in range(1, 11):
    N = int(input())
    arr = [input() for _ in range(8)]
    cnt = 0
    for r in range(8):  # 가로
        for c in range(8-N+1):
            lstc = arr[r][c:c+N]
            if lstc == lstc[::-1]:
                cnt += 1

    for c in range(8):  # 세로
        for r in range(8-N +1):
            lstr = [arr[r + i][c] for i in range(N)]
            if lstr == lstr[::-1]:
                cnt += 1

    print(f'#{tc} {cnt}')