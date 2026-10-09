class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        result = 0
        signs = set(["+","-","*","/"])
        for c in tokens:
            print(f"token:{c}")
            if c not in signs:
                stack.append(c)
            elif c == "+":
                result = int(stack.pop()) + int(stack.pop())
                stack.append(result)
            elif c == "-":
                f = int(stack.pop())
                s = int(stack.pop())
                result = s - f
                stack.append(result)
            elif c == "*":
                f = int(stack.pop())
                s = int(stack.pop())
                result = s * f
                stack.append(result)
            elif c == "/":
                f = int(stack.pop())
                s = int(stack.pop())
                result = s / f
                stack.append(result)
            print("Result")
            print(result)
            print("Stack")
            for n in stack:
                print(n)
            print("_______________")
        return int(stack[0])


            
        