# Leetcode 136. Single Number
# https://leetcode.com/problems/single-number/
# Find the number that appears only once in an array of numbers

from typing import List


class Solution:

    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for n in nums:
            res ^= n
        return res


# ! for testing
nums = [4, 1, 2, 1, 2]
print(Solution().singleNumber(nums))
