# leetcode 74. Search a 2D Matrix
# https://leetcode.com/problems/search-a-2d-matrix/
# search for value in m x n matrix
# matrix is sorted in ascending order from left to right,
# and each row is sorted in ascending order from top to bottom

from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])
        top, bot = 0, ROWS - 1
        while top <= bot:
            row = (top + bot) // 2
            if target > matrix[row][-1]:
                top = row + 1
            elif target < matrix[row][0]:
                bot = row - 1
            else:
                break
        row = (top + bot) // 2
        l, r = 0, COLS - 1
        while l <= r:
            mid = (l + r) // 2
            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        return False


# ! for testing
matrix = [
    [1, 3, 5, 7],
    [10, 11, 16, 20],
    [23, 30, 34, 60]
]
target = 3
print(Solution().searchMatrix(matrix, target))

