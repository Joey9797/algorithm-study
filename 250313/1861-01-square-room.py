import sys
sys.stdin = open("input.txt", "r")

'''
돌아는 가지만 실행시간, 메모리 최악인 코드 ----------------------------------------------------------------
'''

def move(r, c, cnt, sr, sc):
    global max_cnt

    if dp[r][c]:
        if cnt >= max_cnt:
            max_cnt = cnt
            max_rooms.append((max_cnt, rooms[sr][sc]))
            # print(max_rooms)
        return
    
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if 0 <= nr < N and 0 <= nc < N and rooms[nr][nc] == rooms[r][c] + 1:
            move(nr, nc, cnt+1, sr, sc)

def print_ans(max_rooms):
    max_rooms = sorted(max_rooms, reverse=True)
    max_v = max_rooms[0][0]
    min_room_num = 10000000
    for i in max_rooms:
        if i[0] == max_v:
            if i[1] < min_room_num:
                min_room_num = i[1]
        else:
            break
    print(f"#{tc} {min_room_num} {max_v}")


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    rooms = [[*map(int, input().split())] for _ in range(N)]
    dp = [[0]*N for _ in range(N)]
    max_cnt = 0
    max_rooms = []
    dr, dc = [0, 1, 0, -1], [1, 0, -1, 0]
    for r in range(N):
        for c in range(N):
            for i in range(4):
                nr = r + dr[i]
                nc = c + dc[i]
                if 0 <= nr < N and 0 <= nc < N and rooms[nr][nc] == rooms[r][c] + 1:
                    break
            else:
                dp[r][c] = 1

    for r in range(N):
        for c in range(N):
            if dp[r][c] == 0:
                move(r, c, 1, r, c)

    # print(max_rooms)
    print_ans(max_rooms)
    

