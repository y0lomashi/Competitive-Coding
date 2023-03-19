s = input()
res = 1
temp = 1
for i in range(1, len(s)):
    if s[i] == s[i - 1]:
        temp += 1
    else:
        res = max(res, temp)
        temp = 1
print(max(res, temp))
