arr = [100, 200, 201, 204, 208, 304, 305]
friends = [207, 200, 100]
cnt = 0

def binarySearch(t):
    global cnt
    
    s = 0
    e = 6
    while s <= e:
        mid = (s+e)//2
        if t == arr[mid]:
            cnt += 1
            return
        elif t < arr[mid]:
            e = mid - 1
        elif t > arr[mid]:
            s = mid + 1

for score in friends:
    binarySearch(score)
print(cnt)