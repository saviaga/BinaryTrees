# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return
        
        queue = collections.deque([root])
        ans = []
        
        while queue:
            level = []
            for _ in range(len(queue)):
                current = queue.popleft()
                level.append(current.val)
                if current.left:
                    queue.append(current.left)
                if current.right:
                    queue.append(current.right)
            ans.append(level)
        return ans[::-1]
        
        
