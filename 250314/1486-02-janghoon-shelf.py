import sys
sys.stdin = open('input.txt', 'r')
'''
비트연산으로 풀기 ----------------------------------------------------------------
'''
def make_tower():
    global heights, min_height

    for i in range(1, 2**N):
        height = 0
        for j in range(N):
            if i & (1 << j):
                height += heights[j]
            if height >= B:
                if height < min_height:
                    min_height = height
                break

            
T = int(input())
for tc in range(1, T+1):
    N, B = map(int, input().split())    # 점원 수 M, 선반 높이 B
    heights = [*map(int, input().split())]
    min_height = 200001
    make_tower()
    print(f"#{tc} {min_height-B}")