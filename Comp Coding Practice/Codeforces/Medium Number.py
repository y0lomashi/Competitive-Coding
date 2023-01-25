
#  find medium number between given number of inputs
nums = []
for _ in range(int(input())):
  nums = list(map(int, input().split()))
  nums.sort()
  print((nums[1]))

