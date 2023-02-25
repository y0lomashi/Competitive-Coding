
from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        length = len(min(strs, key=len))
        string = ""
        for i in range(length):
            string += strs[0][i]
            for j in range(1, len(strs)):
                if strs[j][i] != string[-1]:
                    return string[:-1]
        
        return string
    

# ! for testing
strs = ["flower", "flow", "flight"]
print(Solution().longestCommonPrefix(strs))
