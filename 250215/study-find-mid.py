arr = [0, 1, 2, 2, 3, 3, 4, 5]
N = len(arr)    # 8
key = 2

def find():
    s = 0
    e = N-1 # 7
    while s <= e:
        mid = (s + e) // 2
        if arr[mid] == key:
            return mid
        elif arr[mid] > key:
            e = mid -1
        else:
            s = mid + 1
    return -1
