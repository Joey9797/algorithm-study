import sys
sys.stdin = open("input.txt", "r")

def make_num(move, r, c):
    if move == 6:
        result.append(''.join(map(str, num)))
        return
    dr, dc = [0, 1, 0, -1], [1, 0, -1, 0]
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if 0 <= nr < 4 and 0 <= nc < 4:
            num.append(board[nr][nc])
            make_num(move+1, nr, nc)
            num.pop()


T = int(input())
for tc in range(1, T+1):
    board = [[*map(int, input().split())] for _ in range(4)]
    result = []
    for r in range(4):
        for c in range(4):
            num = [board[r][c]]
            make_num(0, r, c)
    ans = len(set(result))
    print(f"#{tc} {ans}")