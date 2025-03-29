class RecentCounter:

    def __init__(self):
        self.arr = deque()
        self.index = 0
    def ping(self, t: int) -> int:
        m = [t-3000, t]
        self.arr.append(max(m))
        cnt = 0
        while self.arr:
            if min(m) >self.arr[cnt]:
                self.arr.popleft()
            else:
                break
        return len(self.arr)
        
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)