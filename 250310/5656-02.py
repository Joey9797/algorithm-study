from collections import deque
import copy
import pprint
import sys
sys.stdin = open("input.txt", "r")
'''
재귀함수 사용?
while문 사용?
* 길이 N짜리 조합 만들어야 함
1. 구슬로 맞출 벽돌들 스택에 저장하기 (위에서부터)
2. 하나 골라서 부수기 (visited 1로 바꿔주자)
3. 연쇄작용 처리 (부서진 벽돌 cnt로 세기?)
4. 그 다음으로 맞출 벽돌들 큐에 저장하기
5. 위 행위를 N번 반복하기 (N: 구슬을 쏠 수 있는 횟수)

'''
def bfs(bricks, shoot_cnt):
    global min_left_bricks
    
    Q = deque()
    bricks_c = copy.deepcopy(bricks)
    if shoot_cnt == N or sum([sum(l) for l in bricks_c]) == 0:
        left_bricks = 0
        for c in range(W):
            for r in range(H):
                if bricks_c[r][c] != 0:
                    left_bricks += 1
        min_left_bricks = min(left_bricks, min_left_bricks)
        return

    for c in range(W):
        bricks_c = copy.deepcopy(bricks)
        for r in range(H):
            if bricks_c[r][c] != 0 and (r == 0 or bricks_c[r-1][c] == 0):
                Q.append((r, c))
                break
        while Q and shoot_cnt < N:
            r, c = Q.popleft()
            crush(r, c, bricks_c)
            f_bricks = fall_bricks(bricks_c)
            bfs(f_bricks, shoot_cnt+1)



def crush(r, c, bricks_c):
    power = bricks_c[r][c]
    bricks_c[r][c] = 0
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    for i in range(4):
        for p in range(1, power):
            nr = r + dr[i]*p
            nc = c + dc[i]*p
            if 0 <= nr < H and 0 <= nc < W and bricks_c[nr][nc] != 0:
                if bricks_c[nr][nc] == 1:
                    bricks_c[nr][nc] = 0
                else:
                    crush(nr, nc, bricks_c)
                    

def fall_bricks(bricks):
    f_bricks = [[0]*W for _ in range(H)]
    for c in range(W):
        fr = H-1
        for r in range(H-1, -1, -1):
            if bricks[r][c] != 0:
                f_bricks[fr][c] = bricks[r][c]
                fr -= 1
    return f_bricks

                

T = int(input())
for tc in range(1, T+1):
    N, W, H = [*map(int, input().split())]
    bricks = [list(map(int, input().split())) for _ in range(H)]
    min_left_bricks = 10000
    bfs(bricks, 0)
    print(f"#{tc} {min_left_bricks}")

