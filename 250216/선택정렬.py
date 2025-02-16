# 앞에서부터 정렬됨
arr = [1, 3, 5, 4, 2, 1, 3, 0]
N = len(arr)

for i in range(N-1):
    min_idx = i
    for j in range(i+1, N):
        if arr[j] < arr[min_idx]:
            min_idx = j
    arr[i], arr[min_idx] = arr[min_idx], arr[i]
print(arr)