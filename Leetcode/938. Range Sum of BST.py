# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def sum(node,low,high):
            if node is None:
                return 0
            if (node.val < low):
                return sum(node.right, low,high)
            if (node.val > high):
                return sum(node.left, low,high)
            return sum(node.left, low,high) + node.val + sum(node.right, low,high)
        return sum(root,low,high)
                
        