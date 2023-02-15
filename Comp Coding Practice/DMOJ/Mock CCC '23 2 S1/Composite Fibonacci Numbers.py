import sys
from math import sqrt

t = int(sys.stdin.readline())

for _ in range(t):
    n = int(sys.stdin.readline())
    fib, prev = 8, 5
    comp = False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            comp = True

    while True:
        if n < 8 or fib > n or not comp:
            print("NO")
            break
        elif n == fib:
            print("YES")
            break
        else:
            temp = prev
            prev = fib
            fib += temp
