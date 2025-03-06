import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N, M = list(map(int, input().split()))
    data = [input() for _ in range(N)]
    info = {'0001101':'0', '0011001':'1', '0010011':'2', '0111101':'3', '0100011':'4', '0110001':'5', '0101111':'6', '0111011':'7', '0110111':'8', '0001011':'9'}
    for r in range(N):
        for c in range(M-1, -1, -1):
            if data[r][c] == '1':
                code = data[r][c-55:c+1]
                break
    ans = ''
    for i in range(0, 56, 7):
        ans += info[code[i:i+7]]
    
    ans_sum = 0
    sum_num = 0
    for i in range(0, 8, 2):
        ans_sum += int(ans[i]) + int(ans[i+1])
        sum_num += (int(ans[i]) * 3)
        sum_num += int(ans[i+1]) 
    
    if sum_num % 10 == 0:
        print(f"#{tc} {ans_sum}")
    else:
        print(f"#{tc} {0}")