class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        maxNum = -1
        for n in range(len(arr) -1, -1, -1):
            original = arr[n]
            arr[n] = maxNum
            maxNum = max(maxNum, original)
        return arr
                
            