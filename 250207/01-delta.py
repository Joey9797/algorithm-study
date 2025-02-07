di = [0, +1, 0, -1]
dj = [+1, 0, -1, 0]

N = 2
M = 3
for i in range(N):
    for j in range(M):
        for dir in range(4):
            ni = i + di[dir]
            nj = j + dj[dir]
            if 0<=ni<N and 0<=nj<M:
                print(ni, nj)

# di, dj 배열을 미리 만들어놓지 않은 상태
N = 2
M = 3
for i in range(N):
    for j in range(M):
        for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            ni, nj = i + di, j + dj
            if 0 <= ni < N and 0 <= nj < M:
                print(ni, nj)
