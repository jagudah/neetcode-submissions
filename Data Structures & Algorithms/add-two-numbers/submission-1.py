# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ptr1, ptr2 = l1, l2
        ptr3 = ListNode(-1)
        res = ptr3
        carry = 0
        while ptr1 or ptr2:
            if ptr1 and ptr2:
                ptr3.next = ListNode(ptr1.val + ptr2.val + carry)
                ptr1 = ptr1.next
                ptr2 = ptr2.next
            elif ptr1 and not ptr2:
                ptr3.next = ListNode(ptr1.val + carry)
                ptr1 = ptr1.next
            else:
                ptr3.next = ListNode(ptr2.val + carry)
                ptr2 = ptr2.next
            ptr3 = ptr3.next
            carry = 0

            if ptr3.val >= 10:
                ptr3.val -= 10
                carry = 1
        if carry == 1:
            ptr3.next = ListNode(carry)
        return res.next