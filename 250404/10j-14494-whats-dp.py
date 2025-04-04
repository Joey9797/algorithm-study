def dynamic():
    for r in range(1, n+1):
        for c in range(1, m+1):
            if r == 1:
                dp[r][c] = 1
                continue
            if c == 1:
                dp[r][c] = 1
                continue
            dp[r][c] = dp[r-1][c] + dp[r][c-1] + dp[r-1][c-1]
    return dp[n][m]
            


n, m = map(int, input().split())
dp = [[0]*(m+1) for _ in range(n+1)]
print(dynamic() % (10**9+7))


