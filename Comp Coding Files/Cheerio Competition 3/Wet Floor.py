import sys

n, m = map(int, sys.stdin.readline().split())
diagram = []
for i in range(n):
    row = []
    chars = sys.stdin.readline()
    for k in range(len(chars) - 1):
        row.append(chars[k])
        if chars[k] == "W":

            if k == 0:
                pass
            elif k == m:
                if row[k - 1] == ".":
                    row[k - 1] = "C"
            else:
                if row[k - 1] == ".":
                    row[k - 1] = "C"
            # check vertical cases above
            if i == 0:
                pass
            else:
                if diagram[i - 1][k] == ".":
                    diagram[i - 1][k] = "C"
        if chars[k] == ".":
            if k == 0:
                pass
            else:
                if row[k - 1] == "W":
                    row[k] = "C"
            # check vertical cases below
            if i == 0:
                pass
            else:
                if diagram[i - 1][k] == "W":
                    row[k] = "C"
        
    diagram.append(row)
for row in diagram:
    for val in row:
        sys.stdout.write(val)
    sys.stdout.write("\n")
