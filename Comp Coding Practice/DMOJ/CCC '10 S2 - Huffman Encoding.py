import sys

codes = {}
for _ in range(int(sys.stdin.readline())):
    code = list(map(str, sys.stdin.readline().split()))
    codes[code[1]] = code[0]

message = sys.stdin.readline()
res = ''
encoded = ''
for char in message:
    encoded += char
    if encoded in codes:
        res += codes[encoded]
        encoded = ''

print(res)
