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

        def getLonelyNodesHeler(root, ans):
            if root is None:
                return
            if root.right and not root.left:
                ans.append(root.right.val)
            if root.left and not root.right:
                ans.append(root.left.val)
            getLonelyNodesHeler(root.left, ans)
            getLonelyNodesHeler(root.right, ans)

        ans = []
        getLonelyNodesHeler(root, ans)
        return ans

