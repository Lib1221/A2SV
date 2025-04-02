class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        count = [0]*(max(nums)+2)
        for i in nums:
            count[i]+=1
        for i in range(len(count)):
            if count[i]==0:
                return i
        
        