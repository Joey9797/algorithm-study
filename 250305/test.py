N = 5
arr = [1, 2, 3, 4, 5]
for i in range(N):
    for j in range(i, N-1):
        arr[j] = 7
        print(arr)
        break