import sys
sys.stdin = open("input.txt", "r")
'''
dfs + memoization 으로 품 ----------------------------------------------------------------
'''
def move(r, c):
    if dp[r][c] != -1:  # 방문 했었던 정점이면
        return dp[r][c] # 리턴
    
    dp[r][c] = 1
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if 0 <= nr < N and 0 <= nc < N and rooms[nr][nc] == rooms[r][c] + 1:
            # 가장 긴 길을 찾는 것이므로, 현재(r, c)dp 값과, 다음 노드(nr, nc)를 갔다 온 값 중 더 큰 값을 현재 dp 값으로 한다. 
            dp[r][c] = max(dp[r][c], move(nr, nc) + 1)
            break

    return dp[r][c] # 막다른 길일 때 (for문 들어가서 아무것도 없이 그대로 빠져나왔을 때), 리턴하기



T = int(input())
for tc in range(1, T+1):
    N = int(input())
    rooms = [[*map(int, input().split())] for _ in range(N)]
    dp = [[-1]*N for _ in range(N)] # visited 배열(한 번도 안갔던 길은 -1)
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
    

