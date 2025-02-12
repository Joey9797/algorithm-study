'''
1
9
000304053
243232532
042540453
012450311
252501310
532151550
404542445
055353403
303030115
'''
T = int(input())
for tc in range(1, T + 1):
    N = int(input())  # 배열의 크기
    arr = [[int(num) for num in input()] for _ in range(N)]
    # for _ in range(N):
    #     print([int(num) for num in input()])
    # print(arr)

    # 위쪽 삼각형 먼저
    sum_val = 0
    mid = N // 2  # 중앙의 좌표
    for i in range(mid + 1):
        s = mid - i
        e = mid + i
        for j in range(s, e + 1):
            sum_val += arr[i][j]
    for i in range(mid + 1, N):
        s = mid - (N - 1 - i)
        e = mid + (N - 1 + i)
        for j in range(s, e + 1):
            sum_val += arr[i][j]

    print(f"#{tc} {sum_val}")

    # for r in range(mid + 1):  # 0, 1, ~, 가운데 줄까지 반복
    #     start = mid - r
    #     end = mid + r
    #     for c in range(start, end + 1):  # c=start ~ c=end
    #         sum_val += arr[r][c]
    #
    # # 아래 삼각형
    # for r in range(mid + 1, N):  # mid+1, ~ , N
    #     start = mid - (N - 1 - r)
    #     end = mid + (N - 1 + r)
    #     for c in range(start, end + 1):
    #         sum_val += arr[r][c]