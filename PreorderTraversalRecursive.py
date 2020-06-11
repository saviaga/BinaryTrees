# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        def preorderTraversalHelper(root):
            if root is None:
                return

            self.ans.append(root.val)
            preorderTraversalHelper(root.left)
            preorderTraversalHelper(root.right)

        self.ans = []
        preorderTraversalHelper(root)
        return self.ans