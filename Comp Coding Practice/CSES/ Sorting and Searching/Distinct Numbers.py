n = int(input())
nums = sorted(map(int, input().split()))
res = 1
for i in range(1, len(nums)):
    if nums[i] != nums[i-1]:
        res+=1
print(res)