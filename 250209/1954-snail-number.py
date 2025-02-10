'''
2
3
4
'''
import pprint
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [[0] * N for _ in range(N)]

    num = 1
    for n in range(N // 2 + N % 2):
        for j in range(n, N - n):
            arr[n][j] = num
            num += 1

        for i in range(n + 1, N - n):
            arr[i][N - n - 1] = num
            num += 1

        if N - n - 1 > n:
            for j in range(N - n - 2, n - 1, -1):
                arr[N - n - 1][j] = num
                num += 1

        if N - n - 1 > n:
            for i in range(N - n - 2, n, -1):
                arr[i][n] = num
                num += 1

    result = "\n".join(" ".join(map(str, row)) for row in arr)
    print(f'#{tc}\n{result}')

# for n in range(N):
#     if n == 0:
#         for j in range(N):
#             arr[n][j] = num
#             num += 1
#     for i in range(n + 1, N - n):
#         arr[i][N - n - 1] = num
#         num += 1
#     for j in range(N - n - 2, n - 1, -1):
#         arr[N - n - 1][j] = num
#         num += 1
#     for i in range(N - n - 2, n, -1):
#         arr[i][n] = num
#         num += 1

# for j in range(N):
#     arr[0][j] = 1 + di[0] + dj[0]*j
# for i in range(1, N):
#     arr[i][N-1] = arr[0][N-1] + di[1]*i + dj[1]
# for j in range(N-1):
#     arr[N-1][j] = arr[N-1][N-1] + N-1 + di[2]+ dj[2]*j
# for i in range(1, N-1):
#     arr[i][0] = arr[N-1][0] + N-1 + di[3]*i + dj[3]
#
# for j in range(1, N-1):
#     arr[1][j] = arr[1][0] + j
# for i in range(2, N-2):
#     arr[i][2] = arr[1][2] + N-1 - i
# for j in range(2, N-1):
#     arr[1][j] = arr[1][0] + j


