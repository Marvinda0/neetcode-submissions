class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxarea = 0
        l , r = 0 , len(heights) - 1
        for _ in range(len(heights)):
            area = min(heights[l],heights[r]) * (r-l)
            if area> maxarea:
                maxarea=area
            if heights[l] < heights[r]:
                l += 1
            elif heights[l] > heights[r]:
                r -= 1
            else:
                r -= 1
                l += 1
        return maxarea


        