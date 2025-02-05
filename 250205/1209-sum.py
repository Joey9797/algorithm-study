# tc = int(input())
# arr = list(map(int, input().split()))

# 대각선: 0, 101, 202, ... 99*101 총 100번 더하기
# 세로: 0, 100, 200... 99*100 총 100번 더하기
# 가로: 0~ 99 총 100번 더하기

# dia_idx = []
# for i in range(100):
#     i = 101*i
#     dia_idx.append(i)
#
# ver_idx = []
# for i in range(100):
#     i = 100*i
#     ver_idx.append(i)
#
# hor_idx = []
# for i in range(100):
#     i = 100*i
#     hor_idx.append(i)

T = 10
for tc in range(1, T+1):
    input() # input의 한 줄 씩
    arr = [list(map(list, input().split()))
           for _ in range(100)] # 2차원 배열 (1차원 배열을 담을 배열)

    # 최대값을 구하는 것이 목표
    # 문제의 조건에 따라 임의의 가장 최소의 값(엄청난 음수)을 최대값이라고 가정
    # - 최대값을 구할 때는 최소값으로 초기화
    # - 최소값을 구할 때는 최대값으로 초기화
    max_val = -2 ** 31 # 임의의 엄청난 최소값 생성

    # 가로줄 합 구하기
    for r in range(100):
        max_val = max(max_val, sum(arr[r])) # max_val 과 arr[r]의 총 합 중 더 큰 값을 max_val에 재할당

    # 세로줄 합 구하기
    for c in range(100):
        col_sum = sum(arr[r][c] for r in range(100))
        max_val = max(max_val, col_sum)

    # 대각선1 합 구하기





