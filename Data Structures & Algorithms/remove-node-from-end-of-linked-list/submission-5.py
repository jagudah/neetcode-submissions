# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count, ptr1 = 0, head

        while ptr1:
            ptr1 = ptr1.next
            count += 1
        N = count - n + 1
        
        dummy = ListNode(-1, head)

        prev, curr = None, dummy
        while N > 0:
            prev = curr
            curr = curr.next
            N -= 1
        if curr.next:
            prev.next = curr.next
            curr.next = None
        else:
            prev.next = None
        
        return dummy.next