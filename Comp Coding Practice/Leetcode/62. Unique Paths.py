from functools import cache

# * using memoization


class Solution:
    @cache
    def uniquePaths(self, m: int, n: int) -> int:
        if m == 1 and n == 1:
            return 1
        if m == 0 or n == 0:
            return 0
        return self.uniquePaths(m - 1, n) + self.uniquePaths(m, n - 1)


# ! for testing
m = 3
n = 2
print(Solution().uniquePaths(m, n))
