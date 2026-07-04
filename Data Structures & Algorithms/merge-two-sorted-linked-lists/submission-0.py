# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        mergedList = ListNode()
        mHead = mergedList
        curr1, curr2 = list1, list2

        while curr1 and curr2:
            if curr1.val <= curr2.val:
                mHead.next = curr1
                curr1 = curr1.next
            else:
                mHead.next = curr2
                curr2 = curr2.next
            mHead = mHead.next
        if curr1:
            mHead.next = curr1
        else:
            mHead.next = curr2
        
        return mergedList.next