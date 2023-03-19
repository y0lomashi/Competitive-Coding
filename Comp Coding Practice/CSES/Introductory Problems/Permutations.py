import sys

n = int(sys.stdin.readline())

if n == 2 or n == 3:
    sys.stdout.write("NO SOLUTION")
else:
    odd = list(range(1, n + 1, 2))
    even = list(range(2, n + 1, 2))
    sys.stdout.write(' '.join(map(str, (even+odd))))
