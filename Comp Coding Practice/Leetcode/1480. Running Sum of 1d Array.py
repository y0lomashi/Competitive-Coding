# Leetcode 1480. Running Sum of 1d Array
# https://leetcode.com/problems/running-sum-of-1d-array/
# Given an array nums. We define a running sum of an array as
# runningSum[i] = sum(nums[0]…nums[i]).
# Return the running sum of nums.

from typing import List


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        for i in range(1, len(nums)):
            nums[i] += nums[i-1]
        return nums


# ! for testing
nums = [1, 2, 3, 4]
print(Solution().runningSum(nums))
