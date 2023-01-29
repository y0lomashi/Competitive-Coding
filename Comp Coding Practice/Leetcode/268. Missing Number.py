# Leetcode 268. Missing Number
# https://leetcode.com/problems/missing-number/
# Find the missing number in an array of numbers from 0 to n
# n is the length of the array

from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        numxor = 0
        for i, num in enumerate(nums):
            numxor ^= (i ^ num)
        return numxor ^ (i+1)


# ! for testing
nums = [3, 0, 1]
print(Solution().missingNumber(nums))
