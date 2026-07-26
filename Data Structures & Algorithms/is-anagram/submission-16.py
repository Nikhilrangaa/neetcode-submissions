class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        anagram_map_s = {}
        anagram_map_t = {}

        for c in s:
            if c in anagram_map_s:
                anagram_map_s[c] += 1
            else:
                anagram_map_s[c] = 1
        
        for x in t:
            if x in anagram_map_t:
                anagram_map_t[x] += 1
            else:
                anagram_map_t[x] = 1
        
        if anagram_map_s != anagram_map_t:
            return False
        else:
            return True
        
        