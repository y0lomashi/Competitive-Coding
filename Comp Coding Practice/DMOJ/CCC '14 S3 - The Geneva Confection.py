import sys

resList = []
for _ in range(int(sys.stdin.readline())):
    res = "Y"  # assume it's possible
    stack = [0]  # to avoid edge case where there is no stack to pop from
    carts = []
    for _ in range(int(sys.stdin.readline())):
        cart = int(sys.stdin.readline())
        carts.append(cart)
    for _ in range(len(carts)):
        cart = carts.pop()
        if cart == 1:
            break
        else:
            stack.append(cart)
    next = 2
    while True:
        if carts:
            cart = carts.pop()
            if cart == next:
                next += 1
            elif stack[-1] == next:
                next += 1
                stack.pop()
                carts.append(cart)  # put it back
            else:
                stack.append(cart)
        else:
            if stack[-1] == next:
                stack.pop()
                next += 1
            else:
                res = "N"
                break
            if len(stack) == 1:
                break
        
    resList.append(res)

for res in resList:
    print(res)
