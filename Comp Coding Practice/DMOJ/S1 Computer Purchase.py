# Determine which computer is the best value for money
# Based on performance metric 2R + 3S + D
# R = RAM, S = Speed, D = Drive
# Return the best 2 computers in order of best performance
# if there is a tie, return them in alphabetical order

# ! not finished (not sure why first test case is wrong)

computers = {}
res = []
for _ in range(int(input())):
    name, r, s, d = input().split()
    computers[name] = 2 * int(r) + 3 * int(s) + int(d)

# Sort by performance metric
computers = sorted(computers.items(), key=lambda x: x[1], reverse=True)

try:
    res.append(computers[0])
    res.append(computers[1])
except IndexError:
    pass
# Sort by alphabetical order if performance metric is the same
try:
    if res[0][1] == res[1][1]:
        res = sorted(res, key=lambda x: x[0])
except IndexError:
    pass

try:
    print(res[0][0])
    print(res[1][0])
except IndexError:
    pass
