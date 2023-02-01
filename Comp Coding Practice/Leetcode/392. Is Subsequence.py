# Leetcode 392. Is Subsequence
# https://leetcode.com/problems/is-subsequence/
# Given a string s and a string t, check if s is subsequence of t.


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i, j = 0, 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1
        return i == len(s)


# ! for testing
print(Solution().isSubsequence("abc", "ahbgdc"))
print(Solution().isSubsequence("axc", "ahbgdc"))
