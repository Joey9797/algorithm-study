'''
2
5 3
0 0 1 1 1
1 1 1 1 0
0 0 1 0 0
0 1 1 1 1
1 1 1 0 1
5 3
1 0 0 1 0
1 1 0 1 1
1 0 1 1 1
0 1 1 0 1
0 1 1 1 0
'''
# T = int(input())
# for tc in range(1, T+1):
#     N, K = list(map(int, input().split()))
#     puz = [list(map(int, input().split())) for _ in range(N)]
#     ans = 0
#     for r in range(N):
#         cnt = 0
#         for c in range(N):
#             if puz[r][c] == 1:
#                 cnt += 1
#                 if cnt == K:
#                     ans += 1
#                     if c+1 < N and puz[r][c+1] == 1:
#                         ans -= 1
#             else:
#                 cnt = 0

#     print(ans)

T = int(input())
for tc in range(1, T+1):
    N, K = list(map(int, input().split()))
    puz = [[0] * (N+2)] + [[0] + list(map(int, input().split())) + [0] for _ in range(N)] + [[0] * (N+2)]
    ans = [1] * K
    cnt = 0
    for r in range(1, N+1):
        for c in range(1, N-K+2):
            if puz[r][c:c+K] == ans and puz[r][c+K] == 0 and puz[r][c-1] == 0:
                cnt += 1
    
    for c in range(1, N+1):
        for r in range(1, N-K+2):
            p = []
            if puz[r+K][c] == 0 and puz[r-1][c] == 0:
                for i in range(K):
                    p.append(puz[r+i][c])
                if p == ans:
                    cnt += 1
    print(f'#{tc} {cnt}')
    
