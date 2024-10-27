class MinStack:

    def __init__(self):
        self.stack = []
        self.MIN = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.MIN or self.MIN[-1] >= val:
            self.MIN.append(val)
        
    def pop(self) -> None:
        val = self.stack.pop()
        if val == self.MIN[-1]:
            self.MIN.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.MIN and self.MIN[-1]
# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()