class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        l = Counter(nums)
        return [i for i, j in l.most_common() if j == 2]
        