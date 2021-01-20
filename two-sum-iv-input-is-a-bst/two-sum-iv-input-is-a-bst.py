# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        
        nodes = []
        
        stack = [root]
        
        
        while stack:
            current = stack.pop()
            if k - current.val in nodes:
                return True
            else:
                nodes.append(current.val)
            if current.left:
                stack.append(current.left)
            if current.right:
                stack.append(current.right)
        return False
        
