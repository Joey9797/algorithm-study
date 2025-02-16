arr = [1, 3, 5, 4, 2, 1, 3, 0]
N = len(arr)

for i in range(N-1):    # i는 시작점
    min_idx = i
    for j in range(i+1, N):   # i+1 부터 N-1 까지
        if arr[j] < arr[min_idx]:   # i와 i+1 비교
            min_idx = j
    arr[i], arr[min_idx] = arr[min_idx], arr[i],
print(arr)

