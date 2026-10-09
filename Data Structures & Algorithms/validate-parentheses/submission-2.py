class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        open_brackets = set(["(","[","{"])
        close_brackets = set([")","]","}"])
        for c in s:
            if c in open_brackets:
                stack.append(c)
            if c in close_brackets:
                if len(stack)==0:
                    return False
                top = stack.pop()
                if top == "(" and c != ")":
                    return False
                if top == "[" and c != "]":
                    return False
                if top == "{" and c != "}":
                    return False
        if len(stack) == 0:
            return True
        return False


            
        