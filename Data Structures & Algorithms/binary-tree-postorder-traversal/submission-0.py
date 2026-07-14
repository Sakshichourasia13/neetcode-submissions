
class Solution:
    def postorder(self,root,arr):
        if not root:
            return 
        self.postorder(root.left,arr)
        self.postorder(root.right,arr)
        arr.append(root.val)
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[postt]:
        arr=[]
        self.postorder(root,arr)
        return arr