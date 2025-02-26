'''
1
5 3
1 0 0 1 0
1 1 0 1 1
1 0 1 1 1
0 1 1 0 1
0 1 1 1 0
'''
T = int(input())
for tc in range(1, T+1):
    N, K = list(map(int, input().split()))
    puz = [list(map(int, input().split())) for _ in range(N)]
    ans = 0
    for r in range(N):
        cnt = 0
        for c in range(N):
            if puz[r][c] == 1:
                cnt += 1
                if cnt == K:
                    ans += 1
                    if c+1 < N and puz[r][c+1] == 1:
                        ans -= 1
            else:
                cnt = 0

    print(ans)

# T = int(input())
# for tc in range(1, T+1):
#     N, K = list(map(int, input().split()))
#     puz = [list(map(int, input().split())) for _ in range(N)]
#     ans = [1] * K
#     cnt = 0
#     for r in range(N):
#         for c in range(N-K+1):
#             if c+K < N and puz[r][c:c+K] == ans and puz[r][c+K] != 1:
#                 cnt += 1
    
#     for c in range(N):
#         p = []
#         for r in range(N-K+1):
#             if r+K < N:
#                 for i in range(K):
#                     p.append(puz[r+i][c])
#         if p == ans:
#             cnt += 1
#     print(cnt)
    
