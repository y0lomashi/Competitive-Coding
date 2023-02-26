
a = []
for _ in range(int(input())):
    a.append(int(input()))
a.sort(reverse=True)
per = 0
i, triangles = 0, 0
running = True
if len(a) < 6:
    print(0)
    running = False
while running:
    if a[i] < a[i + 1] + a[i + 2]:
        per += a[i] + a[i + 1] + a[i + 2]
        a.remove(a[i])
        a.remove(a[i])
        a.remove(a[i])
        a.sort(reverse=True)
        triangles += 1
        if triangles == 2:
            print(per)
            break
    else:
        i += 1
        if i == len(a) - 2:
            print(0)
            break
