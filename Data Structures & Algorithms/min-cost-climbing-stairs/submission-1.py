class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost.append(0)
        reach1 = 0
        reach2 = 0
        for i in range(2,len(cost)):
            minNextStep= min(reach1+cost[i-2],reach2+cost[i-1])
            reach1 = reach2
            reach2 = minNextStep
        return reach2