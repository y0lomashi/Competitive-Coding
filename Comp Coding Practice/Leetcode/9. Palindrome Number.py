# Palindrome Number
# https://leetcode.com/problems/palindrome-number/
# Check if a number is a palindrome without converting it to a string


class Solution:

    def isPalindrome(self, x: int) -> bool:
        num = x
        reverse = 0
        while x > 0:
            # This leaves the last digit in x as it is the renmainder of x % 10
            rem = x % 10  # extract the last digit
            # Increase previous reverse by 1 digit and add the last digit
            reverse = reverse * 10 + rem  # append rem to the end of the reversed number
            # Floor division, rounds down to lower integer
            # This drops the last digit in x as it becomes a deciman when divided by 10
            x //= 10  # drop the last digit
        print(reverse)
        if num == reverse:
            print("true")
            return True
        else:
            print("false")
            return False


# Initialize class and print
p = Solution()
p.isPalindrome(x=121)
