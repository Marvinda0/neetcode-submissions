class Solution:
    def calPoints(self, operations: List[str]) -> int:
        total = 0
        stack = []
        for x in operations:
            if x == "+":
                stack.append(stack[-1]+stack[-2])
            elif x == "C":
                stack.pop()
            elif x == "D":
                stack.append(stack[len(stack)-1] * 2)
            else:
                stack.append(int(x))
        for x in stack:
            total += x
        return total