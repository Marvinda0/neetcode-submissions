class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        m = {}
        for s in strs:
            if len(s) < 1 :
                if m.get((0)):
                    m[(0)].append(s)
                else:
                    m[(0)] = [s]
                continue
            count = [0] * 26
            for c in s:

                count[ord(c)-97] +=1
            key = tuple(count)
            if m.get(key):
                m[key].append(s)
            else:
                m[key] = [s]
        return list(m.values())
