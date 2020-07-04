# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:

        def zigzagLevelOrderHelper(root, level, right):
            if root is None:
                return
            if len(self.ans) == level:
                self.ans.append(collections.deque([]))
            if right:
                self.ans[level].append(root.val)
            else:
                self.ans[level].appendleft(root.val)
            right = not right
            zigzagLevelOrderHelper(root.left, level + 1, right)
            zigzagLevelOrderHelper(root.right, level + 1, right)

        self.ans = []
        zigzagLevelOrderHelper(root, 0, True)
        return self.ans
