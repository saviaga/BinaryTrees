# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        def preorderTraversalHelper(root, ans):
            if root is None:
                return
            ans.append(root.val)
            preorderTraversalHelper(root.left, ans)
            preorderTraversalHelper(root.right, ans)

        ans = []
        preorderTraversalHelper(root, ans)
        return ans