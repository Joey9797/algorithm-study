import sys
sys.stdin = open("input.txt", "r")

# 방 번호로만 비교하기 실패!!! 복도를 공유하는 것임!!
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    rooms = sorted([sorted([*map(int, input().split())]) for _ in range(N)])
    total = N
    while rooms:
        s, e = rooms.pop()
        for r in rooms:
            ss, ee = r
            if s > ee:
                total -= 1
                break
    print(f"#{tc} {total}")


    # rooms = []
    # total = N
    # for _ in range(N):
    #     s, e = sorted([*map(int, input().split())])
    #     for ss, ee in rooms:
    #         if s > ee:
    #             total -= 1
    #     rooms.append([s, e])