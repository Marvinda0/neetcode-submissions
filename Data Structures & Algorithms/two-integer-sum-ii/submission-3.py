class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) -1
        for _ in range(len(numbers)):
            sol = numbers[l]+numbers[r]
            if sol == target:
                return [l+1,r+1]
            if sol > target:
                r -= 1
            if sol < target:
                l += 1

        
            
            

        