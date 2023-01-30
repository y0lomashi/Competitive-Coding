# Leetcode 191. Number of 1 Bits
# https://leetcode.com/problems/number-of-1-bits/
# Count the number of 1 bits in an integer


class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n:
            res += n & 1
            n >>= 1
        return res


# ! for testing
# 0b prefix to indicate binary
n = 0b00000000000000000000000000001011
print(Solution().hammingWeight(n))
