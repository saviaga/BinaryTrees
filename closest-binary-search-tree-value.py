# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
        
        def closestValueHelper(root,target):
            if root is None:
                return 
            
            values[root.val] = abs(root.val - target)    
            closestValueHelper(root.left,target)
            closestValueHelper(root.right,target)
            
        values = {}
        closestValueHelper(root,target)
        return min(values, key=values.get)
        
