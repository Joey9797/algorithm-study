T = int(input())
for tc in range(1, T+1):
    N = int(input()) # 버스 노선 개수 N
    info = [list(map(int, input().split())) for _ in range(N)] # 노선 정보
    P = int(input())    # 확인할 버스 정류장 개수
    stop = [0]*5001     # 0 ~ 5000번 까지 있음 (맨 앞 0은 안씀)
    check = [int(input()) for _ in range(P)]
    ans = []
    for s, e in info:
        for i in range(s, e+1):
            stop[i] += 1
    for c in check:
        ans.append(stop[c])
    print(f"#{tc} {' '.join(map(str, ans))}")