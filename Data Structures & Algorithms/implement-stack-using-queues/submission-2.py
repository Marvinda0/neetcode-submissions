from collections import deque

class MyStack:

    def __init__(self):
        self.s = deque()

    def push(self, x: int) -> None:
        if len(self.s) == 0:
            self.s.append(x)
            return None
        print(self.s)
        insert = x
        for i in range(len(self.s)):
            temp = self.s.popleft()
            self.s.append(insert)
            insert = temp
        self.s.append(insert)
        print(self.s)

    def pop(self) -> int:
        return self.s.popleft()
        

    def top(self) -> int:
        return self.s[0]
        

    def empty(self) -> bool:
        if len(self.s)>0:
            return False
        return True
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()