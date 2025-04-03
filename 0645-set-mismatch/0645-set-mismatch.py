class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        num = set(nums)
        another = Counter(nums)
        res = 0
        for i, j in another.most_common(1):
            res = i
        for i in range(1, max(nums)+2):
            if i not in num:
                return [res, i]
        