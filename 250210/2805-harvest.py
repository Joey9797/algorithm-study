'''
5
14054
44250
02032
51204
52212
7
3200021
1000023
3001023
0000004
1010033
3203112
1032100
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
# T = int(input())
# for tc in range(1, T+1):
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
# 왼쪽/위 구하기
arr1 = [[0] * N for _ in range(N)]
for i in range(N):
    for j in range(N):
        arr1[j][N-1-i] = arr[i][j]    # 전치행렬(?) 을 활용하기 위해 배열을 90도 돌려준다.
for i in range(k):
    for j in range(k):
        if i < j:
            sum += arr1[i][j]
# 오른쪽/위 구하기
for i in range(k):
    for j in range(k+1, N):
        nj = j - (k+1)  # 0, 1, 2
        if i > nj:
            sum += arr[i][j]
# 왼쪽/아래 구하기
for i in range(k+1, N):
    for j in range(k):
        ni = i - (k+1)  # 0, 1, 2
        if ni < j:
            sum += arr[i][j]
# 오른쪽/아래 구하기
new_arr2 = [[0] * k for _ in range(k)]
for i in range(k+1, N):
    for j in range(k+1, N):
        new_arr2[j][k -1 -i] = arr[i][j]
for i in range(k):
    for j in range(k):
        if i > j:
            sum += new_arr2[i][j]

# for i in range(k+1, N):
#     for j in range(k+1, N):
#         ni = i - (k+1)
#         nj = j - (k+1)
#         if 0 <= ni < k-1 and 0 <= nj < k-1 and ni != nj:
#             sum += arr[i][j]

print(f"{sum}")
# for i in range(k):
#     for j in range(k):
#         if 0 < i < k and 0 < j < k:
#             sum += arr[i][j]
# for i in range(k):
#     for j in range(k, N):
#         if 0 < i < k and k < j < N-1:
#             sum += arr[i][j]