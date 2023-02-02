# Leetcode 876. Middle of the Linked List
# https://leetcode.com/problems/middle-of-the-linked-list/
# Find the middle node of a linked list
# if 2 middle nodes, return the second middle node

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        return slow


# ! for testing
list1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
# * print the linked list
head = Solution().middleNode(list1)
while head:
    print(head.val)
    head = head.next
