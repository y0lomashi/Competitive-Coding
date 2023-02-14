import sys

for _ in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())
    a = list(map(int, sys.stdin.readline().split()))
    counter = 0
    for i in range(n):
        a = sorted(a)
        if a[i] > 0:
            if a[i] > 1 or i == n - 1:
                a[i] = 0
                counter += 1
            else:
                a[i] -= 1
                a[i + 1] -= 1
                counter += 1
    print(counter)
