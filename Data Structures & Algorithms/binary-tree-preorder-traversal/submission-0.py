
class Solution:
    def preorder(self,root,arr):
        if not root:
            return 
        arr.append(root.val)
        self.preorder(root.left,arr)
        self.preorder(root.right,arr)
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[pret]:
        arr=[]
        self.preorder(root,arr)
        return arr