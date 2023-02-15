import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
q = deque()
taken = [0] * n
rates = []
for _ in range(n):
    rates.append(int(sys.stdin.readline()))

weights = []
for _ in range(m):
    weights.append(int(sys.stdin.readline()))

earned = 0
for i in range(m * 2):
    enter = int(sys.stdin.readline())

    if enter < 0:
        for j in range(n):
            if taken[j] == -enter:
                # Clear the spot
                taken[j] = 0
                if len(q) > 0:
                    next = q.popleft()
                    taken[j] = next
                    earned += rates[j] * weights[next - 1]
                break
    else:
        q.append(enter)
        next = q.popleft()
        for j in range(n):
            if taken[j] == 0:
                    taken[j] = next
                    earned += rates[j] * weights[next - 1]
                    break
        else:
            q.appendleft(next)

print(earned)
