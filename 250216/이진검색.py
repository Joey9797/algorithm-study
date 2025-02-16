arr = [1, 3, 4, 6, 9, 10]
N = len(arr)
key = 3

def find(arr, N, key):
    s = 0
    e = N-1
    while s <= e:
        mid = (s + e) // 2
        if arr[mid] == key:
            return mid
        elif arr[mid] > key:
            e = mid - 1
        else:
            s = mid + 1
    return -1


