"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if root is None:
            return

        ans = []
        stack = [root]

        while stack:
            current = stack.pop()
            ans.append(current.val)
            for child in reversed(current.children):
                stack.append(child)
        return ans