from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        res = dummy = ListNode(0)
        carry = 0
        while l1 or l2 or carry:
            val = 0
            if l1:
                val += l1.val
                l1 = l1.next
            if l2:
                val += l2.val
                l2 = l2.next
            if carry:
                val += 1
                carry = 0
            if val >= 10:
                val -= 10
                carry += 1
            dummy.next = ListNode(val)     
            dummy = dummy.next
        return res.next


# ! for testing
l1 = ListNode(2, ListNode(4, ListNode(9)))
l2 = ListNode(5, ListNode(6, ListNode(4, ListNode(9))))
res = Solution().addTwoNumbers(l1, l2)
while res:
    print(res.val)
    res = res.next

