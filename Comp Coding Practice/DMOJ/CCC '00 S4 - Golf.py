
import sys


# python solution, solved in c++ as well


dist, n = int(sys.stdin.readline()), int(sys.stdin.readline())
clubs = [int(sys.stdin.readline()) for _ in range(n)]

dp = [0] + [dist + 1] * dist

for a in range(1, dist + 1):
    for c in clubs:
        if a - c >= 0:
            dp[a] = min(dp[a], 1 + dp[a - c])

print(f"Roberta wins in {dp[dist]} strokes" if dp[dist] != dist + 1 else "Roberta acknowledges defeat.")

