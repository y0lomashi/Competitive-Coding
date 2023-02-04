import sys

for _ in range(int(sys.stdin.readline())):
    a = sys.stdin.readline()
    res = ""
    counter = 0
    n = sys.stdin.readline()
    if n[0] == "1":
        counter += 1
    for char in n[1:]:
        if char == "1":
            if counter > 0:
                res += "-"
                counter -= 1
            elif counter == 0:
                res += "+"
                counter += 1

        elif char == "0":
            res += "+"
    print(res)
