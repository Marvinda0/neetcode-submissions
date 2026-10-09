class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        Sletters= {}
        for l in s:
            if l in Sletters:
                Sletters[l] +=1
            else:
                Sletters[l] = 1
        Tletters = {}
        for l in t:
            if l in Tletters:
                Tletters[l] +=1
            else:
                Tletters[l] = 1
        print(Tletters)
        print(Sletters)
        return Tletters == Sletters

        
        
            
        
            
            
