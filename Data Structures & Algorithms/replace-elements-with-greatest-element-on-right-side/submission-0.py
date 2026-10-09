class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        maxNum = arr[-1]
        temp = 0
        for n in range(len(arr) -1, -1, -1):
            if arr[n] >= maxNum:
                temp = maxNum
                maxNum = arr[n]
                arr[n] = temp
            else:
                arr[n] = maxNum
        arr[-1] = -1
        return arr
                
            