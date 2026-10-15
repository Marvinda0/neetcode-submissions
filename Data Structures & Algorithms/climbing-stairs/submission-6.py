class Solution:
    def climbStairs(self, n: int) -> int:
        if n <=2:
            return n
        count = 0
        one = 1
        two = 2
        for i in range(2,n):
            count = one + two
            one = two
            two = count
        return count
