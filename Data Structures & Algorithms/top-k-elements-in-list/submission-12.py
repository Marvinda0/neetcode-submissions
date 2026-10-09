class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = [[] for x in (range(len(nums)+1))]
        map = defaultdict(int)
        for num in nums:
            map[num] += 1
        for num, freq in map.items():
            count[freq].append(num) 
        res = []
        for i in range(len(count)-1, 0, -1):
            for n in count[i]:
                res.append(n)
                if len(res) == k:
                    return res

        return 

            
        