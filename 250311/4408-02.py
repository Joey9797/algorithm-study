import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    corridor = [0]*201  
    # 학생이 지나가야 하는 복도 번호 표시
    for _ in range(N):
        s, e = sorted(map(int, input().split()))
        cor_s = (s+1)//2    # 복도 시작번호
        cor_e = (e+1)//2    # 복도 도착번호
        for i in range(cor_s, cor_e+1):
            corridor[i] += 1
    print(f"#{tc} {max(corridor)}")
