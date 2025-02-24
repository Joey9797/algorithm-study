N = int(input())
tri = [[1]] + [[1, 1]] + [[0]*i for i in range(3, N+1)]
# for i in range(2, N):
#     for j in range(1, i):
#         tri[i][j] += tri[i-1][j]
print(tri)