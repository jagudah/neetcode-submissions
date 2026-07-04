# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        leftDepth = 1
        rightDepth = 1
        
        if root.left:
            leftDepth = self.checkDepth(root.left, leftDepth)
        if root.right:
            rightDepth = self.checkDepth(root.right, rightDepth)

        return max(leftDepth, rightDepth)
        
    def checkDepth(self, node, currDepth): 
        currDepth += 1
        l = r = currDepth

        if node.left:
            l = self.checkDepth(node.left, currDepth)
        if node.right:
            r = self.checkDepth(node.right, currDepth)
        
        return max(l, r)