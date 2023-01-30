# Leetcode 724. Find Pivot Index
# https://leetcode.com/problems/find-pivot-index/
# Given an array of integers nums, write a method that returns the "pivot" index of this array.
# We define the pivot index as the index where the sum of the numbers to the left of the index is equal to the sum of the numbers to the right of the index.
# If no such index exists, we should return -1. If there are multiple pivot indexes, you should return the left-most pivot index.

from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        left_sum = 0
        for i in range(len(nums)):
            # this checks if left sum is equal to right sum
            if left_sum == total - left_sum - nums[i]:
                return i
            # prefix sum to calculate left sum faster
            left_sum += nums[i]
        return -1