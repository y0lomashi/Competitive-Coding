# Leetcode 70. Climbing Stairs
# https://leetcode.com/problems/climbing-stairs/
# * Dynamic programming, similar to fiboanacci


class Solution:
    def climbStairs(self, n: int) -> int:
        one, two = 1, 1

        for i in range(n - 1):
            temp = one
            one = one + two
            two = temp

        return one


# ! for testing
n = 3
print(Solution().climbStairs(n))
