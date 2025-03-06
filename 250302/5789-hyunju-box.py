# T = int(input())
# for tc in range(1, T+1):
#     N, Q = list(map(int, input().split()))  # 상자수 N, 작업횟수 Q
#     box = [0]*N
#     info = [list(map(int, input().split())) for _ in range(Q)]
#     for i in range(1, Q+1):
#         L, R = info[i-1]
#         for j in range(L-1, R):
#             box[j] = i
#     print(f"#{tc} {' '.join(map(str, box))}")



T = int(input())
for tc in range(1, T+1):
    N, Q = list(map(int, input().split()))  # 상자수 N, 작업횟수 Q
    box = [0]*N
    for i in range(1, Q+1):
        L, R = list(map(int, input().split()))
        box[L-1:R] = [i]*(R-L+1)
    print(f"#{tc} {' '.join(map(str, box))}")