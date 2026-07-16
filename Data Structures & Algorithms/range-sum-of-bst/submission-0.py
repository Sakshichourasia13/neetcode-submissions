# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        sm=[]
        def traverse(root,sm):
            if not root:
                return
            traverse(root.left,sm)
            if root.val in range(low,high+1):
                sm.append(root.val)
            traverse(root.right,sm)
        traverse(root,sm)
        return sum(sm)