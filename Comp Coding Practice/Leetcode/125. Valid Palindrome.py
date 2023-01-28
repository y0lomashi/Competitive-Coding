# Leetcode Link: https://leetcode.com/problems/valid-palindrome/


class Solution:
    def isPalindrome(self, s: str) -> bool:
        # using join to remove all non-alphanumeric characters
        bareS = ''.join(e for e in s if e.isalnum()).lower()
        return bareS == bareS[::-1]


# ! for testing
s = "A man, a plan, a canal: Panama"
print(Solution().isPalindrome(s))