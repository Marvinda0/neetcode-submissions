class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        m = defaultdict(int)
        buckets = [[] for _ in range(len(nums) + 1)]
        res=[]
        for n in nums:
            m[n] += 1
        for number, counts in m.items():
            buckets[counts].append(number)
        for i in range(len(buckets) - 1, 0, -1):
            for num in buckets[i]:
                res.append(num)
                if len(res) == k:
                    return res





        
        