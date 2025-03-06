import pprint


T = int(input())
N = int(input())
arr = [[0] * N for _ in range(N)]
arr[0][0] = 1
num = 0
sr, sc = 0, 0
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
while num < 16:
    for i in range(N):
        for j in range(i, N-i): 
            num += 1
            sr = dr[i]*j
            sc = dc[i]*j
            arr[sr][sc] = num
pprint.pprint(arr, width=30)
print(sr, sc)
# for i in range(N):
#     num += 1
#     arr[sr][sc+i] = num
# sc = N-1
# for i in range(1, N):
#     num += 1
#     arr[sr+i][sc] = num
# sr = N-1
# for i in range(1, N):
#     num += 1
#     arr[sr][sc-i] = num
# sc = 0
# for i in range(N-1):
#     num += 1
#     arr[sr-i][sc] = num
# sr = 1

