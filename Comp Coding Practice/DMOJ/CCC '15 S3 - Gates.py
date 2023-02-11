import sys

gates = int(sys.stdin.readline())
planes = int(sys.stdin.readline())

airport = [0 for x in range(gates)]
res = 0

for _ in range(planes):
    plane = int(sys.stdin.readline()) - 1

    print(plane)
    while plane >= 0 and airport[plane] > 0:
        save = airport[plane]
        airport[plane] += 1
        plane = plane - save

    if plane < 0:
        break
    else:
        airport[plane] += 1
        res += 1

print(res)
