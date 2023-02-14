import sys

m, n = int(sys.stdin.readline()), int(sys.stdin.readline())
rows = [-1 for _ in range(m)]
cols = [-1 for _ in range(n)]
counter = 0

for _ in range(int(sys.stdin.readline())):
    type, pos = sys.stdin.readline().split()
    pos = int(pos) - 1
    # Flip the sign of the row or column if it is brushed
    # this indicates that the row or column has been painted
    if type == "R":
        rows[pos] *= -1
    else:
        cols[pos] *= -1

for i in range(m):
    for j in range(n):
        # Multiply the overlapping row and column
        # If the product is -1, then the square has been painted Gold
        if rows[i] * cols[j] == -1:
            counter += 1
print(counter)
