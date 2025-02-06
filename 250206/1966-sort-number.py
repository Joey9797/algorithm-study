T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    k = max(arr)
    c = [0] * (k+1)
    final = [0] * N

    for i in range(N):
        c[arr[i]] += 1

    for i in range(1, k+1):
        c[i] += c[i-1]

    for i in range(N-1, -1, -1):
        c[arr[i]] -= 1
        final[c[arr[i]]] = arr[i]


    print(f"#{tc} {' '.join([str(n) for n in final])}")


