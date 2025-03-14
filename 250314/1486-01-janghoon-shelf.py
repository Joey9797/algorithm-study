import sys
sys.stdin = open('input.txt', 'r')
'''
완전탐색(재귀)으로 풀기 ----------------------------------------------------------------
'''
def make_tower(height, i):
    global heights, min_height

    if height >= B:
        if height < min_height:
            min_height = height
        return
    
    if i == N:
        return

    make_tower(height+heights[i], i+1)
    make_tower(height, i+1)


T = int(input())
for tc in range(1, T+1):
    N, B = map(int, input().split())    # 점원 수 M, 선반 높이 B
    heights = sorted([*map(int, input().split())])
    min_height = 200001
    make_tower(0, 0)
    print(f"#{tc} {min_height-B}")