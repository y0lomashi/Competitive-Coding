m, n = 2, 3
indices = [[0,1],[1,1]]

matrix = [[False for i in range(n)]for j in range(m)]
for i in range(len(indices)):
    row = indices[i][0]
    col = indices[i][1]
    for r in range(m):
        if r == row:
            for c in range(n):
                matrix[r][c] = not matrix[r][c]
    for c in range(n):
        if c == col:
            for r in range(m):
                matrix[r][c] = not matrix[r][c]
count = 0
for r in range(m):
    for c in range(n):
        if matrix[r][c] is True:
            count += 1

print(count)
