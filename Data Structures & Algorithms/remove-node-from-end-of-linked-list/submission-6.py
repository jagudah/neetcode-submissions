# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        nodes = 0
        dummy, ptr = ListNode(), head
        dummy.next = head
        while ptr:
            nodes += 1
            ptr = ptr.next
        prev, cur = dummy, head
        while nodes - n > 0:
            prev = cur
            cur = cur.next
            nodes -= 1
        prev.next = cur.next if cur.next else None
        cur.next = None
        return dummy.next