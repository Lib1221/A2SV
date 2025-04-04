class MyQueue:

    def __init__(self):
        self.stack = deque()
        

    def push(self, x: int) -> None:
        self.stack.append(x)
        

    def pop(self) -> int:
        if self.stack == deque():
            return []
        return self.stack.popleft()
        

    def peek(self) -> int:
        return self.stack[0]
        

    def empty(self) -> bool:
        return self.stack == deque()
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()