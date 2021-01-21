# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
        if root is None:
            return
        
        difference = float('inf')
        value = 0
        
        stack = [root]
        ans = []
        
        while stack:
            current = stack.pop()
            if abs(target-current.val) < difference:
                difference = abs(target-current.val)
                value = current.val
                
            if current.right:
                stack.append(current.right)
            if current.left:
                stack.append(current.left)
        return value
        
        
        
        
