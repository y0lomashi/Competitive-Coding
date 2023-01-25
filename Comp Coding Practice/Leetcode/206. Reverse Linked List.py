# Problem: Reverse a singly linked list.
# Solution: Use a prev, curr, and nxt pointer to reverse the linked list.
# Time Complexity: O(n)
# Space Complexity: O(1)
# Leetcode: https://leetcode.com/problems/reverse-linked-list/
# * Also wrote solution in notebook


from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
            
        return prev


# ! for testing
# Nodes put into list format
p = Solution()
p.reverseList(head=ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))) 
