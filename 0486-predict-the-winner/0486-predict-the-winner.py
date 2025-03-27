class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        def play(left, right):
            if left==right:
                return nums[left]
            m = nums[left]- play(left+1, right)
            n = nums[right] - play(left, right-1)
            return max(m, n)
        return play(0, len(nums)-1) >= 0

        