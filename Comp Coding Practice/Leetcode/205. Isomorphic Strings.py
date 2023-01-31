# Leetcode 205. Isomorphic Strings
# https://leetcode.com/problems/isomorphic-strings/
# Given two strings s and t, determine if they are isomorphic.
# Two strings are isomorphic if the characters in s can be replaced to get t.


class Solution:

    def isIsomorphic(self, s: str, t: str) -> bool:
        mapS, mapT = {}, {}
        for i in range(len(s)):
            c1, c2 = s[i], t[i]
            if (c1 in mapS and mapS[c1] != c2
                    or c2 in mapT and mapT[c2] != c1):
                return False
            mapS[c1] = c2
            mapT[c2] = c1
        return True


# ! for testing
print(Solution().isIsomorphic("egg", "add"))
