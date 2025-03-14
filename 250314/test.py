T = int(input())
for tc in range(1, T+1):
    N, B = map(int, input().split())    # 점원 수 M, 선반 높이 B
    heights = sorted([*map(int, input().split())])

    print(heights)