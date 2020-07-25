# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def getLonelyNodes(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        stack = [root]
        ans = []

        while stack:
            current = stack.pop()

            if current.left:
                stack.append(current.left)
                if not current.right:
                    ans.append(current.left.val)

            if current.right:
                stack.append(current.right)
                if not current.left:
                    ans.append(current.right.val)

        return ans