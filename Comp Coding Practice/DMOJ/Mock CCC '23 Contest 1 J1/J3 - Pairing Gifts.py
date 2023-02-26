import sys

n, k, m = map(int, sys.stdin.readline().split())
a = list(map(int, sys.stdin.readline().split())).sort()
b = list(map(int, sys.stdin.readline().split())).sort()
pairs = 0
for i in range(n):
    diff = abs(i + k)
    for j in range(diff, n):
        if a[i] + b[j] == m:
            pairs += 1
            # making sure they won't be used again
            a[i], b[j] = -1 * m, -1 * m
print(pairs)
