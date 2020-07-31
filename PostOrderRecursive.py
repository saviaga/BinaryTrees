# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        def postorderTraversalHelper(root, ans):
            if root is None:
                return
            postorderTraversalHelper(root.left, ans)
            postorderTraversalHelper(root.right, ans)
            ans.append(root.val)

        ans = []
        postorderTraversalHelper(root, ans)
        return ans
