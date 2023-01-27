# Leetcode 217. Contains Duplicate
# https://leetcode.com/problems/contains-duplicate/

from typing import List


class Solution:

    def containsDuplicate(self, nums: List[int]) -> bool:
        nums2 = list(set(nums))
        if len(nums) == len(nums2):
            print("false")
            return False
        else:
            print("true")
            return True


# ! for testing
nums = [1, 2, 3, 1]
Solution().containsDuplicate(nums)
