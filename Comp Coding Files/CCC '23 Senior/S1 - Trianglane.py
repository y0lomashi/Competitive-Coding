import sys

# * Good solution full points

n = int(sys.stdin.readline())
grid = []

for _ in range(2):
    grid.append(list(map(int, sys.stdin.readline().split())))

perimeter = 0
for r in range(2):
    for c in range(n):
        if grid[r][c] == 1:
            perimeter += 3
            if c > 0 and grid[r][c - 1] == 1:
                perimeter -= 2
            if r == 1 and c % 2 == 0 and grid[r - 1][c] == 1:
                perimeter -= 2

print(perimeter)