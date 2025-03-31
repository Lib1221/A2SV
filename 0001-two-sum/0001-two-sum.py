class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashset = {}
        for i in range(len(nums)):
            if target - nums[i] in hashset:
                return [i, hashset[target - nums[i]]]
            hashset[nums[i]] = i

        