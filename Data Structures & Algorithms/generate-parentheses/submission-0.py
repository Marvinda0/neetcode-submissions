class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = []
        def backtrack(openN, CloseN):
            if openN == CloseN == n:
                res.append("".join(stack))
                return
            if openN < n:
                stack.append("(")
                backtrack(openN+1,CloseN)
                stack.pop()
            if CloseN < openN:
                stack.append(")")
                backtrack(openN,CloseN+1)
                stack.pop()
        backtrack(0,0)
        return res
            

        

        