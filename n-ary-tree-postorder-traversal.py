"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
​
class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if root is None:
            return
        
        stack = [(root,False)]
        res = []
        
        while stack:
            current,visited = stack.pop()
            if visited:
                res.append(current.val)
            else:
                stack.append((current,True))
                for c in reversed(current.children):
                    stack.append((c,False))
        return res
        
