import pprint

N = int(input())
arr = [[0] * N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if j == 0:
            arr[i][j] = 1
pprint.pprint(arr, width=20)