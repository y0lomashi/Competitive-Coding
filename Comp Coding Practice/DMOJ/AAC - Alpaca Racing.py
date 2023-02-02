# AAC - Alpaca Racing
# https://dmoj.ca/problem/aac1p2
import sys
import math

n, d, k, x = map(int, sys.stdin.readline().split())
speeds = []
for i in range(n):
    speeds.append(int(sys.stdin.readline()))
speeds.sort()
p = int(sys.stdin.readline())
x = (100 - x)/100
while k:
    for i, s in enumerate(speeds):
        if p > s:
            pass
        else:
            speeds[i] = math.floor(s * x)
            k -= 1
        if k == 0:
            break
    if p > speeds[-1]:
        break

if p > speeds[-1]:
    print("YES")
else:
    print("NO")
