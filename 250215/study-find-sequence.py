arr = [1, 3, 5, 4, 2, 1, 3, 0]
N = len(arr)
key = 5

#-------------------------------------------------------------------------
# 정렬이 안되어있는 경우의 순차 검색
i = 0
idx = 0
while i < N and arr[i] != key:  # i가 N-1 을 넘거나, key와 같다면 break
    i += 1
if i < N:
    idx = i
    result = 1
else:
    result = 0
print(result, idx)


#-------------------------------------------------------------------------
# 정렬이 되어있는 경우의 순차 검색
arr = sorted(arr)
i = 0
while i < N and arr[i] < key:   # i가 N-1을 넘거나, arr[i]가 key와 같아지면 break
    i += 1
if i < N and arr[i] == key:
    result = 1
    idx = i
else:
    result = -1
print(result, idx)


#-------------------------------------------------------------------------
# 정렬이 되어있는 경우의 순차 검색 (for문 사용)
arr = sorted(arr)
print(arr)
def find(arr, N, key):
    for i in range(N):
        if arr[i] == key:
            return i, 1
        elif arr[i] > key:
            return -1
    return -1
print(find(arr, N, key))