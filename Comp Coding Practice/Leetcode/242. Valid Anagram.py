# Problem: Given two strings s and t , write a function to determine if t is an anagram of s.
# Leetcode Link: https://leetcode.com/problems/valid-anagram/
#  Hashmap solution

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        mapS, mapT = {}, {}

        for i in range(len(s)):
            # .get() returns the value for the given key.
            # If key is not available then returns the value 0.
            mapS[s[i]] = mapS.get(s[i], 0) + 1  # add 1 to the counter of the character key
            mapT[t[i]] = mapT.get(t[i], 0) + 1
        for c in mapS:
            if mapS[c] != mapT[c].get(c, 0):
                return False
        return True


# ! for testing
s = "anagram"
t = "nagaram"
print(Solution().isAnagram(s, t))