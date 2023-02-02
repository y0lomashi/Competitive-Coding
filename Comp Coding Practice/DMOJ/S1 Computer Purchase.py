# Determine which computer is the best value for money
# Based on performance metric 2R + 3S + D
# R = RAM, S = Speed, D = Drive
# Return the best 2 computers in order of best performance
# if there is a tie, return them in alphabetical order

# ! not finished

computers = {}
r, s, d = 0, 0, 0
for _ in range(int(input())):
    name, r, s, d = input().split()
    computers[name] = 2 * int(r) + 3 * int(s) + int(d)

# Sort by performance metric
computers = sorted(computers.items(), key=lambda x: x[1], reverse=True)

# Sort by alphabetical order if performance metric is the same
try:
    if computers[0][1] == computers[1][1]:
        computers = sorted(computers, key=lambda x: x[0])
except IndexError:
    pass

try:
    print(computers[0][0])
except IndexError:
    pass
try:
    print(computers[1][0])
except IndexError:
    pass
