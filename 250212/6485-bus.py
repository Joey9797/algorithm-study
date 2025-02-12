T = int(input())
for tc in range(1, T+1):
    N = int(input()) # 버스 노선의 개수
    bus = [list(map(int, input().split())) for _ in range(N)] # 버스 노선 시작점, 끝점
    # [[2, 100] ,[50, 3000], [100, 600]]
    P = int(input()) # 정류장의 개수
    station = [int(input()) for _ in range(P)] # 정류장의 번호
    # [100, 2, 300, 1000, 200]
    S = len(station)

    cnt = [0] * 5001
    for line in bus:
        cnt[line[0] : line[1]+1] = [i + 1 for i in cnt[line[0] : line[1]+1]]

    station_cnt = [cnt[i] for i in station]
    result = ' '.join(list(map(str, station_cnt)))
    print(f'#{tc} {result}')

