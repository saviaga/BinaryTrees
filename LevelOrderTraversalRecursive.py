# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:

        def levelOrderHelper(root, level):
            if root is None:
                return
            if len(self.ans) == level:
                self.ans.append([])

            self.ans[level].append(root.val)
            levelOrderHelper(root.left, level + 1)
            levelOrderHelper(root.right, level + 1)

        self.ans = []
        levelOrderHelper(root, 0)
        return self.ans