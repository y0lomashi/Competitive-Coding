post = []
while True:
    pre = list(map(str, input().split()))
    if pre[0] == '0':
        break
    stack = []
    pre.reverse()
    for i in pre:
        if i in ['+', '-']:
            a = stack.pop()
            b = stack.pop()
            stack.append(a + ' ' + b + ' ' + i)
        else:
            stack.append(i)
    post.append(stack[0])

for i in post:
    print(i)
