import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    candy = [*map(int, input().split())]
    cnt = 0
    if candy[0] < 1 or candy[1] < 2 or candy[2] < 3:
        print(f"#{tc} {-1}")
        continue
    if candy[1] >= candy[2]:
        cnt += candy[1] - candy[2] + 1
        candy[1] = candy[2] - 1
    if candy[0] >= candy[1]:
        cnt += candy[0] - candy[1] + 1
        candy[0] = candy[1] - 1
    print(f"#{tc} {cnt}")
