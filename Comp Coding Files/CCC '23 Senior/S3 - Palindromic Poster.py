import sys
import random

# ! did not finish

n, m, r, c = map(int, sys.stdin.readline().split())

if r == n and c != m or r != n and c == m:
    print("IMPOSSIBLE")
    sys.exit()
grid = [[chr(ord("a") + random.randint(1, 25)) for _ in range(m)]
        for _ in range(n)]
for i in range(n):
    if r > 0:
        for j in range(m):
            grid[i][j] = "b"
        r -= 1
    if c > 0:
        for j in range(n):
            grid[j][i] = "b"
        c -= 1
    else:
        break

for i in range(n):
    print(*grid[i], sep="")