import sys
sys.stdin = open('input.txt', 'r')


def choose_and_sum(num, i):
    global cnt

    if num > K:
         return 
    
    if i == N:
        if num == K:
            cnt += 1
        return

    choose_and_sum(num+arr[i], i+1)
    choose_and_sum(num, i+1)

    

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    arr = list(map(int, input().split()))
    cnt = 0
    choose_and_sum(0, 0)
    print(f"#{tc} {cnt}")