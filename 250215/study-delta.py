a = [1, 2, 3, 4, 5]
arr = [a for _ in range(5)]
N = len(arr)
k = 2

#-------------------------------------------------------------------------
# 중심을 기준으로 십자모양의 최대합 구하기 (중심값도 더해야 함)/(배열을 넘어서는 값은 더하면 안됨)
mx = 0
for r in range(N):
    for c in range(N):
        sm = arr[r][c]
        for i in range(1, k+1):
            for dr, dc in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
                nr = r + dr * i
                nc = c + dc * i
                if 0 <= nr < N and 0 <= nc < N :
                    sm += arr[nr][nc]
        if sm > mx:
            mx = sm


#-------------------------------------------------------------------------
# 전치행렬 (대각선을 기준으로 좌우가 같은 것)
mid = []
right = []
left = []
for i in range(N):
    mid.append(arr[i][i])
    for j in range(N):
        # 대각선 기준 오른쪽 위
        if i < j:
            right.append(arr[i][j])
        if i > j:
            left.append(arr[i][j])

print(mid)
print(right)
print(left)

#-------------------------------------------------------------------------
# 대각선 / 방향 구하기
mid = []
for i in range(N):
    mid.append(arr[i][N-i-1])
print(mid)
