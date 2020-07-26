"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Solution:
    def preorder(self, root: 'Node') -> List[int]:

        def preorderHelper(root,ans):
            if root is None:
                return
            ans.append(root.val)
            for child in root.children:
                preorderHelper(child,ans)

        ans = []
        preorderHelper(root,ans)
        return ans
