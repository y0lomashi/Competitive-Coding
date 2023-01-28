# ! Very important
# * Binary Search
# * Remember that the array is sorted
# Use the middle element to compare with the target
# If the middle element is greater than the target, then the target must be in the left half
# If the middle element is less than the target, then the target must be in the right half
# Repeat the process until the target is found or the array is empty
# Time complexity: O(log n)
# Space complexity: O(1)

from typing import List


class Solution:

    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1

        return -1


# ! for testing
nums = [-1, 0, 3, 5, 9, 12]
target = 9
print(Solution().search(nums, target))
