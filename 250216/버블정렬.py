# 뒤에서부터 정렬된다. 시간복잡도 O(n제곱)
arr = [1, 3, 5, 4, 2, 1, 3, 0]
N = len(arr)

for i in range(N-1, 0, -1):
    for j in range(i):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]
print(arr)