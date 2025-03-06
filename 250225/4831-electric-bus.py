T = int(input())
for tc in range(1, T+1):
    K, N, M = list(map(int, input().split()))
    # K = 충전 시 최대로 이동가능한 정류장수
    # N = 종점 번호
    # M = 정류장 개수
    charge_n = list(map(int, input().split()))
    station = [0] * (N+1+K)
    for n in charge_n:
        station[n] = 1

    cnt = 0
    t = 0
    while t < N:
        if station[t + K] == 1:
            cnt += 1
            t += K
        if t >= N:
            break
        elif station[t + K] == 0:
            t += K
            if t >= N:
                break
            for k in range(1, K):
                if station[t - k] == 1:
                    t -= k
                    cnt += 1
                    break
            else:
                cnt = 0
                break
    print(f'#{tc} {cnt}')