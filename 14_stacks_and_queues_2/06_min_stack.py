class MinStack:
    def __init__(self):
        self.stack = []
        self.mini_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.mini_stack:
            self.mini_stack.append(min(self.mini_stack[-1], val))
        else:
            self.mini_stack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.mini_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.mini_stack[-1]
