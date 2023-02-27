# Leetcode 46. Permutations
# https://leetcode.com/problems/permutations/
# Given a collection of distinct integers, return all possible permutations.


from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # Result array
        res = []
        # Base return case because we are popping letters recursively
        # Eventually nums will only have 1 left so we return then add back
        if len(nums) == 1:
            return [nums[:]]

        for i in range(len(nums)):
            # Take off first num in array
            n = nums.pop(0)
            # Recursive call for remaining letters
            perms = self.permute(nums)
            # add n to all returned values from recursive call
            for perm in perms:
                perm.append(n)
            # adding the values to result
            res.extend(perms)
            # adding number we popped from front to back of array
            nums.append(n)
        return res


# ! for testing
nums = [1, 2, 3]
print(Solution().permute(nums))
