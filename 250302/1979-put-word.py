'''
1
5 3
1 0 0 1 0
1 1 0 1 1
1 0 1 1 1
0 1 1 0 1
0 1 1 1 0'''
T = int(input())
for tc in range(1, 1+T):
    N, K = list(map(int, input().split()))  # 퍼즐 크기 N, 단어 길이 K
    puz = [list(map(int, input().split())) for _ in range(N)]
    ans = 0
    for r in range(N):
        cnt = 0
        for c in range(N):
            if puz[r][c] == 1:
                cnt += 1
                if cnt == K:
                    ans += 1
                    if c+1 > N or (c+1 < N and puz[r][c+1] == 1) :
                        ans -= 1
                        cnt = 0
            else:
                cnt = 0
    for c in range(N):
        cnt = 0
        for r in range(N):
            if puz[r][c] == 1:
                cnt += 1
                if cnt == K:
                    ans += 1
                    if r+1 > N or (r+1 < N and puz[r+1][c] == 1) :
                        ans -= 1
                        cnt = 0
            else:
                cnt = 0
    print(ans)

