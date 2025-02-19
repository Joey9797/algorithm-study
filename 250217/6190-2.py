T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = sorted(list(map(int, input().split())))

    max_v = 0
    for n in range(1, N):
        for m in range(n):
            if max_v < arr[n] * arr[m]:
                a = arr[n]
                b = arr[m]
                n_max_str = str(arr[n] * arr[n-1])
                for i in range(1, len(n_max_str)):
                    if int(n_max_str[i]) < int(n_max_str[i - 1]):
                        break
                else:
                    max_v = arr[n] * arr[n-1]

    result = max_v
    if max_v == 0:
        result = -1
    print(f'#{tc} {result}')