# Leetcode 21. Merge Two Sorted Lists
# https://leetcode.com/problems/merge-two-sorted-lists/
# Merge two sorted linked lists and return it as a new list.
# The new list should be made by splicing together the nodes of the first two lists

from typing import Optional


class ListNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def mergeTwoLists(self, list1: Optional[ListNode],
                      list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy
        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next

        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2
        
        return dummy.next


# ! for testing
list1 = ListNode(1, ListNode(2, ListNode(4)))
list2 = ListNode(1, ListNode(3, ListNode(4)))


# * print the linked list
head = Solution().mergeTwoLists(list1, list2)
while head:
    print(head.val)
    head = head.next

