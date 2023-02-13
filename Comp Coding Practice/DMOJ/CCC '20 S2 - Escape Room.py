

# Breadth First Search
# Starting from end point and checking if you can reach the entry point
# ! TLE for last couple batches

import sys
import collections

rows, cols = int(sys.stdin.readline()), int(sys.stdin.readline())
grid = []
for _ in range(rows):
    grid.append(list(map(int, sys.stdin.readline().split())))


def bfs(r, c):
    q = collections.deque()
    # setting grid value to "V" if it has been visited
    grid[r][c] = "V"
    q.append((r, c))
    while q:
        row, col = q.popleft()
        calc = (row + 1)*(col + 1)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] != "V" and calc == grid[r][c]:
                    print(grid)

                    # This means we reached the starting point
                    if r == 0 and c == 0:
                        return "yes"
                    q.append((r, c))
                    grid[r][c] = "V"
    return "no"


lastRow, lastCol = rows - 1, cols - 1
print(bfs(lastRow, lastCol))
