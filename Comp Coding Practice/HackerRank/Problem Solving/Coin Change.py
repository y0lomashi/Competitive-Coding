
def getWays(n, c):
    # Write your code here
    dp = [n + 1] * (n + 1)
    dp[0] = 0
    
    for a in range(1, n + 1):
        for i in c:
            if a - i >= 0:
                dp[a] = min(dp[a], 1 + dp[a - i])
    return dp[a]

print(getWays(4, [1, 2, 3]))
