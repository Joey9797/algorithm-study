arr = [1, 3, 5, 4, 2, 1, 3, 0]
N = len(arr)    # 8
k = 3 # 3번째로 작은 원소

def find(arr, k):
    for i in range(k):
        min_idx = i
        for j in range(i+1, N):
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[min_idx], arr[i] = arr[i], arr[min_idx]
    return arr[k-1]
print(find(arr, k))