# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:

        if root is None:
            return

        ans = []
        queue = collections.deque([root])

        right = False
        while queue:
            level = collections.deque([])
            for _ in range(len(queue)):
                current = queue.popleft()
                if right:
                    level.appendleft(current.val)
                else:
                    level.append(current.val)
                if current.left:
                    queue.append(current.left)
                if current.right:
                    queue.append(current.right)
            ans.append(level)
            right = not right
        return ans
