import sys


value = {}
for _ in range(int(sys.stdin.readline())):
    key = int(sys.stdin.readline())
    if key not in value:
        value[key] = 1
    else:
        value[key] += 1

values = sorted(value.items(), key=lambda x: x[1], reverse=True)

diff = abs(values[0][0] - values[1][0])

print(diff)