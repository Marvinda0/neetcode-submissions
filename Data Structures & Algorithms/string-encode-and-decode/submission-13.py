class Solution:

    def encode(self, strs: list[str]) -> str:
        enc=""
        for s in strs:
            enc+=(str(len(s)))
            enc+="#"
            enc+=s
        return enc

    def decode(self, s: str) -> list[str]:
        res = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1  
            length = int(s[i:j])  
            ins = s[j+1:j+1+length]
            res.append(ins)
            i = j+length+1
        return res

