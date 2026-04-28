import collections
class MinStack:

    def __init__(self):
        self.stack = collections.deque()
        self.min1 = collections.deque()

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.min1 or val <= self.min1[-1]:
            self.min1.append(val)

    def pop(self) -> None:
        if self.stack[-1] == self.min1[-1]:
            self.min1.pop()
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min1[-1]
