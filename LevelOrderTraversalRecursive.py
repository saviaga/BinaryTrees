# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:

        def levelOrderHelper(root, level,ans):
            if root is None:
                return
            if len(ans) == level:
                ans.append([])

            ans[level].append(root.val)
            levelOrderHelper(root.left, level + 1,ans)
            levelOrderHelper(root.right, level + 1,ans)

        ans = []
        levelOrderHelper(root, 0,ans)
        return ans