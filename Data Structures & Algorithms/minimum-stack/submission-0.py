class MinStack:
    def __init__(self):
        self._stack = []
        self._min = None   
        self._top = None   

    def push(self, val: int) -> None:
        self._stack.append(val)
        if self._min is None or val < self._min:
            self._min = val
        self._top = val

    def pop(self) -> int:
        if not self._stack:
            raise IndexError("pop from empty stack")
        out = self._stack.pop()
        self._top = self._stack[-1] if self._stack else None
        self._min = min(self._stack) if self._stack else None
        return out

    def top(self) -> int:
        return self._top

    def getMin(self) -> int:
        return self._min

        
