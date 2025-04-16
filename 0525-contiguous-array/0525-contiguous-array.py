class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if nums[i] == 0:
                nums[i] = -1
        dict1 = {}
        list1 = [0]
        list1.extend(list(accumulate(nums)))
        l = 0
        for i in range(len(list1)):
            if list1[i] in dict1:
                l = max(abs(i-dict1[list1[i]]), l)
            else:
                dict1[list1[i]] = i
        return l
        