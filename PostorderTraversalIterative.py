# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if root is None:
            return
        ans = []

        stack = [(root, False)]

        while stack:
            current, visited = stack.pop()
            if visited:
                ans.append(current.val)
            else:
                stack.append((current, True))
                if current.right:
                    stack.append((current.right, False))
                if current.left:
                    stack.append((current.left, False))
        return ans
