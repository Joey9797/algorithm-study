import sys
sys.stdin = open("input.txt", "r")

def move(r, c):
    if dp[r][c] != -1:
        return dp[r][c]
    
    dp[r][c] = 1
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if 0 <= nr < N and 0 <= nc < N and rooms[nr][nc] == rooms[r][c] + 1:
            dp[r][c] = max(dp[r][c], move(nr, nc) + 1)
            break

    return dp[r][c] # 막다른 길 다다랐을때, 리턴하기



T = int(input())
for tc in range(1, T+1):
    N = int(input())
    rooms = [[*map(int, input().split())] for _ in range(N)]
    dp = [[-1]*N for _ in range(N)]
    max_cnt = 0
    max_room_num = -1
    dr, dc = [0, 1, 0, -1], [1, 0, -1, 0]
    for r in range(N):
        for c in range(N):
            move(r, c)
    
    for r in range(N):
        for c in range(N):
            if dp[r][c] > max_cnt:
                max_cnt = dp[r][c]
                max_room_num = rooms[r][c]
            elif dp[r][c] == max_cnt:
                max_room_num = min(max_room_num, rooms[r][c])
    print(f"#{tc} {max_room_num} {max_cnt}")
    

