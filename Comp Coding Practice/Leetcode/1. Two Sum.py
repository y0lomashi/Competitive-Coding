# Description: Given an array of integers, return indices of the two numbers such that they add up to a specific target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# Leetcode Link: https://leetcode.com/problems/two-sum/
# Hashmap solution


from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {} # val : index
        for i, n in enumerate(nums):
            diff = target - n
            if diff in hashmap:
                print([hashmap[diff], i])
                return [hashmap[diff], i]
            hashmap[n] = i
        return


# ! for testing
nums = [2, 7, 11, 15]
target = 9
Solution().twoSum(nums, target)
