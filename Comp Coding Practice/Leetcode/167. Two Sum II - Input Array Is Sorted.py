
from typing import List


class Solution:

    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1
        while l < r:
            calc = numbers[l] + numbers[r]
            if calc == target:
                return [l + 1, r + 1]
            elif calc < target:
                l += 1
            elif calc > target:
                r -= 1


# ! for testing
numbers = [2, 7, 11, 15]
target = 9
print(Solution().twoSum(numbers, target))

