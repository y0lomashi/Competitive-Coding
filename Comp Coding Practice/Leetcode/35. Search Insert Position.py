from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # no len(nums) - 1, as we might need to insert at the end of the array
        left, right = 0, len(nums)
        while left < right:
            mid = (left + right) //2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid
        return left
    


# ! for testing
nums = [1, 3, 5, 6]  # expected output: 2
target = 5
print(Solution().searchInsert(nums, target))
