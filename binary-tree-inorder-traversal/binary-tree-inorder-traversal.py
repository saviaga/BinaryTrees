# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        
        if root is None:
            return
        
        stack = []
        res = []
        current = root
        while current:
            stack.append(current)
            current = current.left
            while current == None and stack:
                current = stack.pop()
                res.append(current.val)
                current = current.right
        return res
        
    
        
