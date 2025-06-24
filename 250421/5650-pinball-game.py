import sys
sys.stdin = open('input.txt', 'r')

dr, dc = (0, 1, 0, -1), (1, 0, -1, 0)
def play(r, c):
    for i in range(4):
        



T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [[*map(int, input().split())] for _ in range(N)]
    dp = [[-1]*N for _ in range(N)]
    for r in range(N):
        for c in range(N):
            if arr[r][c] == 0:
                for i in range(4):
                    sr, sc = r, c
                    pr, pc = 0, 0
                    while pr != sr and pc != sc:
                        
