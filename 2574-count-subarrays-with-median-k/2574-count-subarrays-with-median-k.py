class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        balance = 0
        prefix_count = defaultdict(int)
        prefix_count[0] = 1
        total = 0
        found = False
        for num in nums:
            if num < k:
                balance -= 1
            elif num > k:
                balance += 1
            else:
                found = True
            if found:
                total += prefix_count[balance] + prefix_count[balance - 1]
            else:
                prefix_count[balance] += 1
        return total