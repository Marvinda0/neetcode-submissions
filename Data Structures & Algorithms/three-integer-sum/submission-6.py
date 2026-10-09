class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sol = []
        nums.sort()
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            l, r = i + 1, len(nums) - 1
            tar = -nums[i]
            while l < r:
                total = nums[l] + nums[r]
                if total == tar:
                    sol.append([nums[i], nums[l], nums[r]])

                    # ✅ Skip duplicate left values
                    while l < r and nums[l] == nums[l + 1]:
                        l += 1
                    # ✅ Skip duplicate right values
                    while l < r and nums[r] == nums[r - 1]:
                        r -= 1

                    # Move both pointers after recording solution
                    l += 1
                    r -= 1

                elif total < tar:
                    l += 1
                else:
                    r -= 1

        return sol
            
        
         
