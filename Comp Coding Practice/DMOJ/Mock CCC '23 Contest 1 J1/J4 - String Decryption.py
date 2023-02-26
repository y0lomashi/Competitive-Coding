import sys

# Use ascii values to convert letters to indexes in the alphabet
goal = int(sys.stdin.readline())
b = list(sys.stdin.readline().strip('\n'))
base = ord('a') - 1
asCount = 0
res = []
for i in range(len(b)):
    if b[i] == '*':
        asCount += 1
    else:
        goal -= ord(b[i]) - base
        res.append(b[i])

running = True
wtf = True
if asCount == 0 and goal != 0 or asCount >= 1 and goal == 0:
    print("Impossible")
    # pass the while loop
    running = False
    wtf = False


while running:
    if goal - asCount >= 26:
        res.append('z')
        goal -= 26
    elif asCount == 1:
        res.append(chr(base + goal))
        goal = 0
        running = False
    else:
        res.append('a')
        goal -= 1
    asCount -= 1
if wtf:
    res.sort()
    for i in res:
        print(i, end="")
    print()
