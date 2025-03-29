class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        stack = deque()
        maxDeque = deque()  
        minDeque = deque() 
        mini = 0
        for i in nums:
            stack.append(i)
            while maxDeque and maxDeque[-1] < i:
                maxDeque.pop()
            maxDeque.append(i)
            while minDeque and minDeque[-1] > i:
                minDeque.pop()
            minDeque.append(i)
            while maxDeque[0] - minDeque[0] > limit:
                if stack[0] == maxDeque[0]: 
                    maxDeque.popleft()
                if stack[0] == minDeque[0]: 
                    minDeque.popleft()
                stack.popleft()
            mini = max(mini, len(stack))

        return mini
