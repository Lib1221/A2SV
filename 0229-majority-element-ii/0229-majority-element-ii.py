class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        res = []
        l = len(nums)
        nums = Counter(nums)
        for i, j in nums.most_common():
            if j > l/3:
                res.append(i)
            e
        return res
        