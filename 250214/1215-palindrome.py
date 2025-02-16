T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [input() for _ in range(8)]
    cnt = 0
    mid = N // 2
    for r in range(8):  # 가로
        for c in range(8 - mid):
            if N % 2 == 1:  # 회문 길이가 홀수일때
                if N == 1:
                    cnt += 1
                elif arr[r][c:mid] != arr[r][c+N-1:c+mid:-1]: # [c+mid+1:c+N]
                    continue
                else:
                    cnt += 1
            else:   # 회문 길이가 짝수일때
                if arr[r][c:c+mid] != arr[r][c+N-1:c+mid-1:-1]:  # [c+mid:c+N]
                    continue
                else:
                    cnt += 1

    for c in range(8):  # 세로
        for r in range(8 - N +1):
            if N % 2 == 1:  # 회문 길이가 홀수일때
                mid_arr1 = [arr[r + i][c] for i in range(mid)]
                mid_arr2 = [arr[r + i][c] for i in range(mid + 1, N)]
                if N == 1:
                    cnt += 1
                if mid_arr1[::-1] != mid_arr2:
                    continue
                else:
                    cnt += 1
            else:   # 회문 길이가 짝수일때
                mid_arr1 = [arr[r + i][c] for i in range(mid)]
                mid_arr2 = [arr[r + i][c] for i in range(mid, N)]
                if mid_arr1[::-1] != mid_arr2:
                    continue
                else:
                    cnt += 1
    print(f'#{tc} {cnt}')