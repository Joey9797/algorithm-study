T = int(input())
for tc in range(1, T+1):
    N, M, K = list(map(int, input().split()))

    time = sorted(list(map(int, input().split())))
    arr = [0] * (max(time) + 1)
    result = 'Possible'
    boong = 0
    for i in range(len(arr)):
        arr[i] = boong
        if i % M == 0 and i > 0:
            boong += K
            arr[i] = boong
        for c in time:
            if i == c:
                boong -= 1
                arr[i] = boong
        if boong < 0:
            result = 'Impossible'
            break

    # result = 'Possible'
    # if -1 in arr:
    #     result = 'Impossible'
    print(f"#{tc} {result}")
