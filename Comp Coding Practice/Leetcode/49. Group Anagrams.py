# Leetcode 49. Group Anagrams
# https://leetcode.com/problems/group-anagrams/
# Given an array of strings, group anagrams together.

from typing import List
from collections import defaultdict


class Solution:
        def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
            res = defaultdict(list)
            for s in strs:
                count = [0] * 26

                for c in s:
                    count[ord(c) - ord('a')] += 1
                
                res[tuple(count)].append(s)
            return res.values()


# ! for testing
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(Solution().groupAnagrams(strs))
