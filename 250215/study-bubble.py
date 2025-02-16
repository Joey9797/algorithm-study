arr = [1, 3, 5, 4, 2, 1, 3, 0]
N = len(arr)

#-------------------------------------------------------------------------
# 오름차순 정렬
# for i in range(N):
#     for j in range(1, N-i):
#         if arr[j] < arr[j-1]:
#             arr[j-1], arr[j] = arr[j], arr[j-1]
# print(arr)

for i in range(N-1, 0, -1): # [1 ~ N-1] 범위를 정하는 부분. 범위가 0일 수는 없음. 1부터 시작!!
    for j in range(i):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]
print(arr)



#-------------------------------------------------------------------------
# 내림차순 정렬
# for i in range(N):
#     for j in range(1, N-i):
#         if arr[j] > arr[j-1]:
#             arr[j], arr[j-1] = arr[j-1], arr[j]
# print(arr)

for i in range(N-1, 0, -1): # [1, N] = 1 ~ N-1
    for j in range(i):
        if arr[j] < arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]
print(arr)