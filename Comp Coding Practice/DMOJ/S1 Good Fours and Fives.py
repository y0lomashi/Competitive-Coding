# Find number of times a number can be formed using 4 and 5
# https://dmoj.ca/problem/ccc01s1
# wrote solution in notebook

# Input
n = int(input())
# Output
counter = 0
while n >= 0:
    if n % 5 == 0:
        counter += 1
    n -= 4

print(counter)