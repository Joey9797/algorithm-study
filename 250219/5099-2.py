T = int(input())
for tc in range(1, T+1):
    N, M = list(map(int, input().split()))
    che = list(map(int, input().split()))
    num = [i for i in range(1, M+1)]
    piz = {}    # 피자를 번호:치즈수 형태의 딕셔너리로 저장한다
    for c, n in list(zip(num, che)):
        piz[c] = n

    ov = [i for i in range(1, N+1)] # 오븐이 꽉 찰 때까지 피자를 넣는다
    f = N   # f는 오븐에 넣은 피자와 안넣은 피자를 구분하기 위해 사용할 변수.
    # 1, 2, 3 번 피자를 오븐에 넣었으므로, 현재 f는 3

    done = 0
    is_done = False
    while not is_done:
        for j in range(N):
            if ov[j] in piz:
                piz[ov[j]] //= 2
            if ov[j] in piz and piz[ov[j]] == 0 and f < M:
                f += 1
                ov[j] = f
            elif ov[j] in piz and piz[ov[j]] == 0 and f == M:
                done += 1
                ov[j] = -1
            if done == N-1:
                is_done = True
                break
    print(f'#{tc} {max(ov)}')



# N, M = list(map(int, input().split()))
# che = list(map(int, input().split()))
# num = [i for i in range(1, M+1)]
# piz = {}
# for c, n in list(zip(num, che)):
#     piz[c] = n
# print(piz)
# # {1: 7, 2: 2, 3: 6, 4: 5, 5: 3}
#
# ov = [0] * N
# f = 0
# for i in range(N): # 오븐에 첫 피자 넣기
#     f += 1
#     ov[i] = f
# print(ov)
# is_done = False
# while not is_done:
#     for j in range(len(ov)):
#         piz[ov[j]] //= 2
#         if piz[ov[j]] == 0 and f < M:
#             f += 1
#             ov[j] = f
#         elif piz[ov[j]] == 0 and f == M:
#             ov.remove(ov[j])
#         if len(ov) == 1:
#             result = ov[0]
#             is_done = True
#             break
# print(ov[0])