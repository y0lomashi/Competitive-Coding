import sys

# ! TLE 5/15 points

n = int(sys.stdin.readline())
mountains = list(map(int, sys.stdin.readline().split()))
res = []

for i in range(n):

    # dummy large number
    asym = 10000000000
    l, r = 0, n - i - 1
    running = True

    while running:
        lT, rT = (n - 1) // 2 - 1, (n - 1) // 2 + 1
        calc = 0
        while lT > l or rT < r:
            value = abs(mountains[lT] - mountains[rT])
            calc += value
            if calc > asym:
                break
            lT -= 1
            rT += 1
        if calc == 0:
            res.append(calc)
            break
        asym = min(asym, calc)
        r += 1
        l += 1

        if r > n - 1:
            res.append(asym)
            break

res.reverse()
print(*res)
