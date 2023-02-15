import sys

n = int(sys.stdin.readline())
tides = list(map(int, sys.stdin.readline().split()))
tides.sort()
a, b = (n-1)//2, (n-1) // 2
for i in range(n // 2):
    print(tides[a], end=" ")
    print(tides[b + 1], end=" ")
    a -= 1
    b += 1

if n % 2 == 1:
    print(tides[0])
