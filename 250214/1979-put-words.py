T = int(input())
for tc in range(1, T+1):
    N, K = list(map(int, input().split())) # N=가로세로길이 K=단어 길이
    pzl = [list(map(int, input().split()))+[0] for _ in range(N)]
    pzl.append([0]*(N+1))

    w = [1] * K
    cnt = 0
    i = j = 0
    while i < N:
        if j + K <= N and pzl[i][j:j+K] == w and pzl[i][j+K] == 0:
            cnt += 1

        j += 1
        if j >= N:
            j = 0
            i += 1

    i = j = 0
    while j < N:
        if i + K <= N and [pzl[j + jj][i] for jj in range(K)] == w and pzl[j+K][i] == 0: # jj = 0, 1, 2
            cnt += 1

        i += 1
        if i >= N:
            i = 0
            j += 1
    print(f'#{tc} {cnt}')

#------------------------------------------------------------------------
# 내코드 (위에건 gpt)
# w = [1] * K
# cnt = 0
# i = j = 0
# while i < N:
#     if j + K <= N and pzl[i][j:j+K] == w and pzl[i][j+K] == 0:
#         cnt += 1
#     else:
#         if j + K <= N:
#             j += 1
#         else:
#             i += 1
#             j = 0
# i = j = 0
# while i < N:
#     if j + K <= N and [pzl[j + jj][i] for jj in range(K)] == w and pzl[j+K][i] == 0: # jj = 0, 1, 2
#         cnt += 1
#     else:
#         if j + K <= N:
#             j += 1
#         else:
#             i += 1
#             j = 0
# print(cnt)

