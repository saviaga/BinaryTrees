# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        
        if root is None:
            return
        
        stack = [root]
        value_sum = 0
        
        while stack:
            current = stack.pop()
            if current.val >=low and current.val <=high:
                value_sum+=current.val
            if current.right:
                stack.append(current.right)
            if current.left:
                stack.append(current.left)
        return value_sum
                
        
        
    
