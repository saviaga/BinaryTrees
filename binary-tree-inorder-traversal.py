# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        
        def inorderTraversalHelper(root):
            if root is None:
                return
            inorderTraversalHelper(root.left)
            res.append(root.val)
            inorderTraversalHelper(root.right)
        
        res = []
        inorderTraversalHelper(root)
        return res
​
        
