def find(arr, key):
    for i in range(key):
        max_idx = i
        for j in range(i+1, N):
            if arr[j] > arr[max_idx]:
                max_idx = j
        arr[i], arr[max_idx] = arr[max_idx], arr[i]
    return arr[key-1]

arr = [1, 4, 2, 6, 10, 0]
N = len(arr)
key = 3 # 3번쨰로 큰 숫자

print(find(arr, key))