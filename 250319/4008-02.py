import sys
sys.stdin = open("input.txt", "r")
'''
연산자 개수 줄이기 + 재귀 ----------------------------------------------------------------
'''
def calculate(i, num):
    global max_v, min_v

    if i == N-1:
        if num < min_v:
            min_v = num
        if num > max_v:
            max_v = num
        return 
    
    for j in range(4):
        if op_cnt[j]: # and i+1 < N
            op_cnt[j] -= 1
            if j == 0:
                calculate(i+1, num + nums[i+1])
            elif j == 1:
                calculate(i+1, num - nums[i+1]) 
            elif j == 2:
                calculate(i+1, num * nums[i+1])  
            elif j == 3:
                if num < 0:
                    calculate(i+1, -(-num // nums[i+1]))
                else:
                    calculate(i+1, num // nums[i+1])
            op_cnt[j] += 1



T = int(input())
for tc in range(1, T+1):
    N = int(input())
    op_cnt = list(map(int, input().split()))
    ops = ['+', '-', '*', '/']
    nums = list(map(int, input().split()))
    max_v = -100000000
    min_v = 100000000
    calculate(0, nums[0])
    print(f"#{tc} {max_v - min_v}")