# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        
        
        def POHelper(root):
            if root!=None:
                POHelper(root.left)
                POHelper(root.right)
                self.ans.append(root.val)
            
            
        self.ans=[]
        POHelper(root)
        return self.ans
