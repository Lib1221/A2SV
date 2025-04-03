# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def dfs(right, left):
            if not right and not left:
                return True
            if not right or not left or right.val != left.val:
                return False
            return dfs(right.left, left.right) and dfs(left.left, right.right)
        return dfs(root.right, root.left)
        