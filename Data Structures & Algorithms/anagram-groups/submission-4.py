from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = defaultdict(list)  # Dictionary where values are lists
        
        for word in strs:
            # Create a frequency count of letters (26 letters for lowercase a-z)
            count = [0] * 26
            for char in word:
                count[ord(char) - ord('a')] += 1  # Count character occurrences
            
            key = tuple(count)  # Convert list to tuple (hashable)
            anagram_map[key].append(word)  # Store word in the correct group
        
        return list(anagram_map.values())  # Convert defaultdict to list of lists



