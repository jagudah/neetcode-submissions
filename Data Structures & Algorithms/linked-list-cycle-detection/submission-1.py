# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        valCounter = {}
        currNode = head

        while currNode:
            if valCounter.get(currNode, 0) > 0:
                return True
            valCounter[currNode] = 1
            currNode = currNode.next
        
        return False