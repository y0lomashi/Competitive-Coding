import sys

for _ in range(int(input())):
    nums = map(int, sys.stdin.readline().split("+"))
    print(sum(nums))
