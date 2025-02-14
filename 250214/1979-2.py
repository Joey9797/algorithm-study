# 검은색(0)을 만나면 => cnt를 0으로 초기화
# 흰색(1)을 만나면 => cnt += 1

T = int(input())  # 테스트 케이스 수
for tc in range(1, T + 1):
    N, K = list(map(int, input().split()))
    arr = [list(map(int, input().split())) for _ in range(N)]
    # N: 배열의 크기
    # K: 연속된 빈칸(1)의 길이

    ans = 0  # 조건을 만족하는 갯수(정확히 길이가 K인 1)

    # 가로검사
    for r in range(N):
        cnt = 0
        for c in range(N):
            if arr[r][c] == 1:
                cnt += 1
                # K에 딱 맞는 것을 찾으려면
                # 그 뒤가 1이면 안됨
                if cnt == K:  # cnt가 K에 일치하면
                    ans += 1  # 정답 개수 +1
                    if c + 1 < N and arr[r][c + 1] == 1:  # 만약 그 다음 수가 1이면
                        ans -= 1  # 원상복구

            else:
                cnt = 0

                # 세로검사
    for c in range(N):
        cnt = 0
        for r in range(N):
            if arr[r][c] == 1:
                cnt += 1
                # K에 딱 맞는 것을 찾으려면
                # 그 뒤가 1이면 안됨
                if cnt == K:  # cnt가 K에 일치하면
                    ans += 1  # 정답 개수 +1
                    if r + 1 < N and arr[r + 1][c] == 1:  # 만약 그 다음 수가 1이면
                        ans -= 1  # 원상복구

            else:
                cnt = 0

    print(f"#{tc} {ans}")