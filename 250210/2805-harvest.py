'''
5
14054
44250
02032
51204
52212
#4
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
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, list(input()))) for _ in range(N)]
    k = N // 2
    sum = arr[k][k]
    # 십자모양 구하기
    for di, dj in [[0, 1], [-1, 0], [0, -1], [1, 0]]:
        for c in range(1, k+1):
            ni = k + di*c
            nj = k + dj*c
            sum += arr[ni][nj]
    # 왼쪽/위 삼각부분 구하기
    arr1 = [[0] * k for _ in range(k)]
    for i in range(k):
        for j in range(k):
            arr1[i][j] = arr[j][k-1-i]    # i < j 인 요소만 sum에 더할 수 있도록 기존 배열을 90도 돌린 새로운 배열 arr1을 만든다.
    for i in range(k):
        for j in range(k):
            if i < j:
                sum += arr1[i][j]
    # 오른쪽/위 삼각부분 구하기
    for i in range(k):
        for j in range(k+1, N):
            nj = j - (k+1)  # 0, 1, 2
            if i > nj:
                sum += arr[i][j]
    # 왼쪽/아래 삼각부분 구하기
    for i in range(k+1, N):
        for j in range(k):
            ni = i - (k+1)  # 0, 1, 2
            if ni < j:
                sum += arr[i][j]
    # 오른쪽/아래 삼각부분 구하기
    arr2 = [[0] * k for _ in range(k)]
    for i in range(k):
        for j in range(k):
            arr2[i][j] = arr[j + k + 1][N - 1 - i]  # i > j 인 요소만 sum에 더할 수 있도록 기존 배열을 90도 돌린 새로운 배열 arr2를 만든다.
    for i in range(k):
        for j in range(k):
            if i > j:
                sum += arr2[i][j]

    print(f"#{tc} {sum}")
# for i in range(k):
#     for j in range(k):
#         if 0 < i < k and 0 < j < k:
#             sum += arr[i][j]
# for i in range(k):
#     for j in range(k, N):
#         if 0 < i < k and k < j < N-1:
#             sum += arr[i][j]