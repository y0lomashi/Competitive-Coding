from typing import Optional


# had to add boilerplate code to get the it to run


class Node:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def isPalindrome(self, head: Node) -> bool:
        list1 = []
        curr = head
        while curr:
            list1.append(curr.val)
            curr = curr.next
        if list1 == list1[::-1]:
            print("True")
            return True
        else:
            print("False")
            return False


# ! for testing
p = Solution()
p.isPalindrome(head=Node(1, Node(2, Node(2, Node(1)))))
