class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        m = defaultdict(int)
        pairs=[]
        res=[]
        for n in nums:
            m[n] += 1
        for num, count in m.items():
            pairs.append([count,num])
        pairs.sort()
        res = [pairs[len(pairs)-i-1][1] for i in range(k)]
        return res

        
        