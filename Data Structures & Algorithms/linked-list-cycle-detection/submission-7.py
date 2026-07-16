# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        hare = tort = head if head else None

        while hare:
            hare = hare.next.next if hare.next else 0
            tort = tort.next if tort.next else 1

            if tort is hare:
                return True
        
        return False