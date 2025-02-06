'''
가로 길이는 항상 100으로 주어진다.
모든 위치에서 상자의 높이는 1이상 100이하로 주어진다.
덤프 횟수는 1이상 1000이하로 주어진다.
주어진 덤프 횟수 이내에 평탄화가 완료되면 더 이상 덤프를 수행할 수 없으므로 그 때의 최고점과 최저점의 높이 차를 반환한다 (주어진 data에 따라 0 또는 1이 된다).

2
5 8 3 1 5 6 9 9 2 2 4

D = 2 (덤프횟수)
V = 11 (가로길이)
1 <= Ai <= 9 (상자 높이)

834
42 68 35 1 70 25 79 59 63 65 6 46 82 28 62 92 96 43 28 37 92 5 3 54 93 83 22 17 19 96 48 27 72 39 70 13 68 100 36 95 4 12 23 34 74 65 42 12 54 69 48 45 63 58 38 60 24 42 30 79 17 36 91 43 89 7 41 43 65 49 47 6 91 30 71 51 7 2 94 49 30 24 85 55 57 41 67 77 32 9 45 40 27 24 38 39 19 83 30 42
1 <= D <= 1000 (덤프횟수)
V = 100 (가로길이)
1 <= Ai <= 100 (상자 높이)
'''
T = 10
for tc in range(1, T+1):
    D = int(input())
    arr = list(map(int, input().split()))

    while D > 0:
        min_idx = 0
        max_idx = 0
        for i in range(100):
            if arr[i] < arr[min_idx]:
                min_idx = i
            if arr[i] > arr[max_idx]:
                max_idx = i
        arr[min_idx] += 1
        arr[max_idx] -= 1

        if arr[max_idx] - arr[min_idx] <= 1:
            break

        D -= 1

    min_idx = 0
    max_idx = 0
    for i in range(100):
        if arr[i] < arr[min_idx]:
            min_idx = i
        if arr[i] > arr[max_idx]:
            max_idx = i

    print(f'#{tc} {arr[max_idx] - arr[min_idx]}')

