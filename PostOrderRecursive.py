# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        def postorderTraversalHelper(root):
            if root is None:
                return

            postorderTraversalHelper(root.left)
            postorderTraversalHelper(root.right)
            self.ans.append(root.val)

        self.ans = []
        postorderTraversalHelper(root)
        return self.ans
