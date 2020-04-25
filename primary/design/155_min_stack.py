

class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self._array = [0 for _ in range(10)]
        self._top = -1
        self._aux_stack = []

    def push(self, x: int) -> None:
        if self.empty():
            self._aux_stack.append(x)
        self._top += 1
        self._array[self._top] = x
        if x <= self._aux_stack[-1]:
            self._aux_stack.append(x)

    def pop(self) -> None:
        if not self.empty():
            if self.top() == self._aux_stack[-1]:
                self._aux_stack.pop()
            self._top -= 1
            return self._array[self._top+1]

    def top(self) -> int:
        if not self.empty():
            return self._array[self._top]

    def getMin(self) -> int:
        if not self.empty():
            return self._aux_stack[-1]

    def empty(self):
        return True if self._top == -1 else False


obj = MinStack()
print(obj.pop())  # None
obj.push(3)
print(obj.pop())  # 3
obj.push(3)
obj.push(2)
obj.push(1)
print(obj.getMin())  # 1
print(obj.pop())  # 1
print(obj.getMin())  # 2
# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
