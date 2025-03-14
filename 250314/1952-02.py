import sys
sys.stdin = open("input.txt", "r")
'''
DP로 풀기 ----------------------------------------------------------------
'''
T = int(input())
for tc in range(1, T+1):
    D1, M1, M3, Y1 = map(int, input().split()) # 1일, 1달, 3달, 1년
    days = [0] + [*map(int, input().split())]
    min_cost = float('inf')
    dp = [0]*13
    for i in range(1, 13):
        if i < 3:
            dp[i] = min(dp[i-1] + D1*days[i], dp[i-1] + M1, Y1)
        else:
            dp[i] = min(dp[i-1] + D1*days[i], 
                        dp[i-1] + M1,
                        dp[i-3] + M3,
                        Y1)
    print(f"#{tc} {dp[12]}")
    
    
