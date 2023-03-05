import sys


t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    # get all inputs in line separated by space that are length n - 1
    a = list(map(str, sys.stdin.readline().split()))
    i = 0
    while i < len(a):
        if len(a[i]) != n-1:
            del a[i]
            i -= 1
        i += 1
    if a[0] == a[1][::-1]:
        print("YES")
    else:
        print("NO")
