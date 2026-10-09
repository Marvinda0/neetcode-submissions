class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        count_of_nums = {}
        for num in nums:
            if num in count_of_nums:
                return True
            count_of_nums[num] = 0
        return False
