class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letters = {}
        letters1={}
        for c in s:
            letters[c] = letters.get(c,0) + 1
        for c in t:
            letters1[c] = letters1.get(c,0) + 1
        if letters == letters1:
            return True
        return False
        