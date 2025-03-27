# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def solve(start,end):
            if start > end:
                return None

            mid = (start + end)//2
            left = solve(start,mid-1)
            right = solve(mid+1,end)

            return TreeNode(nums[mid],left,right)

        return solve(0,len(nums)-1)