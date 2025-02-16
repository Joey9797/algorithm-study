arr = [1, 3, 5, 4, 2, 6, 0]
N = len(arr)
key = 3
# i = 0
# while i < N and arr[i] != key:
#     i += 1
# if i < N:
#     result = 1
#     index = i
# else:
#     result = 0

# def find(arr, N, key):
#     arr = sorted(arr)
#     for i in range(N):
#         if arr[i] == key:
#             return 1
#         elif arr[i] > key:
#             return 0
#     return 0

arr = sorted(arr)
i = 0
while i < N and arr[i] < key:
    i += 1
if i < N and arr[i] == key:
    result = 1
    index = i
else:
    result = 0