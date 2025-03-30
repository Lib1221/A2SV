class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        maxsum = minSum = res = 0
        for i in nums:
            maxsum = max(i, i+maxsum)
            minSum = min(i, i+minSum)
            res = max(res, abs(maxsum), abs(minSum))
        return res
