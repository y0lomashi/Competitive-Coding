
list = []
for _ in range(int(input())):
    command = input().split()
    if command[0] == "insert":
        list.insert(int(command[1]), int(command[2]))
    if command[0] == "print":
        print(list)
    if command[0] == "append":
        list.append(int(command[1]))
    if command[0] == "remove":
        list.remove(int(command[1]))
    if command[0] == "sort":
        list.sort()
    if command[0] == "pop":
        list.pop()
    if command[0] == "reverse":
        list.reverse()
