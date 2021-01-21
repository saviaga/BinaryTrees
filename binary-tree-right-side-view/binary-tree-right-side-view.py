# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        
        if root is None:
            return
        queue = collections.deque([root])
        ans = []
        r_side = []
        
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
        for elem in ans:
            r_side.append(elem[-1])
        return r_side
            
                
        
