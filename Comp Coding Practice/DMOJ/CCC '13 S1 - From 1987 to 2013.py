import sys

start = int(sys.stdin.readline())
while True:
    cont = False
    count = {}
    start += 1

    for s in str(start):

        if s in count:
            count[s] += 1
        else:
            count[s] = 1

    for key in count:
        if count[key] > 1:
            cont = True
            break
    if cont:
        pass
    else:
        break

print(start)
