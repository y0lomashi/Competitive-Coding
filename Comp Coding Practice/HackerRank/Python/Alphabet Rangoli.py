import string

letters = string.ascii_lowercase
n = int(input())
list = []
for i in range(n):
    s = "-".join(letters[i:n])
    # reverse the string and add the remaining letters
    list.append((s[::-1] + s[1:]).center(n * 4 - 3, "-"))
for j in reversed(range(n)):
    print(list[j])
for x in range(1, n):
    print(list[x])
    