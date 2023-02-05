# Leetcode 20. Valid Parentheses
# https://leetcode.com/problems/valid-parentheses/


class Solution:

    def isValid(self, s: str) -> bool:
        # Using stack
        stack = []
        close_to_open = {")": "(", "]": "[", "}": "{"}
        for char in s:
            if char in close_to_open:
                # if stack is not empty and last element in stack is matching
                if stack and stack[-1] == close_to_open[char]:
                    stack.pop()
                else:
                    return False
            elif char in close_to_open.values():
                stack.append(char)
        # if stack is empty return true, else false
        return True if stack == [] else False


# ! for testing
s = Solution()
print(s.isValid("()"))
print(s.isValid("()[]{}"))
print(s.isValid("(]"))