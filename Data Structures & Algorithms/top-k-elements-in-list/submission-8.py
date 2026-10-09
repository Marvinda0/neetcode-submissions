class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        length = len(nums)
        res = []
        fmap = defaultdict(int)
        for num in nums:
            fmap[num] +=1
        while(k>0 and length>0):
            max_key = max(fmap, key=fmap.get)
            res.append(max_key)
            del fmap[max_key]
            k -=1
            length -=1
        return res
        