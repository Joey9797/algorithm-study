N, k = map(int, input().split())

for i in range(1<<N):
    for j in range(N):
        if i & (1<<j):
            print(arr[j], end=',')
