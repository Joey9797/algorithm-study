import sys
sys.stdin = open("input.txt", "r")
'''
visited 사용 + 재귀로 풀기
실패!!!!!! ----------------------------------------------------------------
'''
def calculate(i, num):
    global max_v, min_v

    if i == N-1:
        if num < min_v:
            min_v = num
        if num > max_v:
            max_v = num
        return 
    
    for j in range(N-1):
        if not visited[j] and i+1 < N:
            visited[j] = 1
            if operator[j] == '+':
                calculate(i+1, num + nums[i+1])
            elif operator[j] == '-':
                calculate(i+1, num - nums[i+1]) 
            elif operator[j] == '*':
                calculate(i+1, num * nums[i+1])  
            elif operator[j] == '/':
                calculate(i+1, num // nums[i+1])

            visited[j] = 0



T = int(input())
for tc in range(1, T+1):
    N = int(input())
    op_cnt = list(map(int, input().split()))
    ops = ['+', '-', '*', '/']
    operator = [ops[i] for i in range(4) for _ in range(op_cnt[i])]
    nums = list(map(int, input().split()))
    max_v = -100000000
    min_v = 100000000
    visited = [0] * (N-1)
    calculate(0, nums[0])
    print(max_v, min_v)