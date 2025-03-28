class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        count = [0]*(abs(min(nums))+max(nums)+1)
        x = abs(min(nums))
        res = []
        for i in nums:
            count[i+x]+=1
        for i, j in enumerate(count):
            s = i-x
            res.extend([s]*j)
        return res

        