from collections import deque
import sys
sys.stdin = open("input.txt", "r")

def calculate(num, cnt):    # 숫자 num, 연산횟수 cnt
    q = deque([(num, cnt)])
    visited = {num} # 지금까지 만든 숫자 저장

    while q:
        num, cnt = q.popleft()
        
         # 연산 후에도 백만 이하의 자연수고, 지금까지 만든 숫자가 아니라면
        if 1 <= num +1 <= 1000000 and num +1 not in visited:   
            if num +1 == M:     # 그와중에 만든 숫자가 M이랑 같다면
                return cnt+1    # 함수 종료(연산횟수 리턴)
            q.append((num+1, cnt+1))  # M이 아니라면 q에 저장
            visited.add(num+1)      # 방금 만든 숫자 visited에 저장

        if 1 <= num -1 <= 1000000 and num -1 not in visited:
            if num -1 == M:
                return cnt+1
            q.append((num-1, cnt+1))
            visited.add(num-1)

        if 1 <= num *2 <= 1000000 and num *2 not in visited:
            if num *2 == M:
                return cnt+1
            q.append((num*2, cnt+1))
            visited.add(num*2)

        if 1 <= num -10 <= 1000000 and num -10 not in visited:
            if num -10 == M:
                return cnt+1
            q.append((num-10, cnt+1))
            visited.add(num-10)
        


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    print(f"#{tc} {calculate(N, 0)}")