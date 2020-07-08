"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Solution:
    def preorder(self, root: 'Node') -> List[int]:

        def preorderHelper(root):
            if root is None:
                return
            self.ans.append(root.val)
            for child in root.children:
                preorderHelper(child)

        self.ans = []
        preorderHelper(root)
