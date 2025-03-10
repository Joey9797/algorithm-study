import sys
sys.stdin = open("input.txt", "r")
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    wires = [[*map(int, input().split())]]
    cnt = 0
    for _ in range(N-1):
        s, e = [*map(int, input().split())]
        for w in wires:
            ss, ee = w
            if (s < ss and e > ee) or (s > ss and e < ee):
                cnt += 1
        wires.append([s, e])
    print(f"#{tc} {cnt}")