# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        linkedListLength = 0
        ptr1 = head

        while ptr1:
            linkedListLength += 1
            ptr1 = ptr1.next
        
        prev, curr = None, head
        currIndex = 0
        targetIndex = linkedListLength - n

        while curr:
            if currIndex == targetIndex:
                if prev is None:
                    temp = curr.next
                    curr.next = None
                    curr = None
                    return temp
                else:
                    prev.next = curr.next
                    curr.next = None
                    return head
            else:
                temp = curr
                curr = curr.next
                prev = temp
                currIndex += 1
        
        return prev
