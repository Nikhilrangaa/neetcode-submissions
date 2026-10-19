class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        anagram_map_s = {}
        anagram_map_t = {}

        for string in s:
            if string not in anagram_map_s:
                anagram_map_s[string] = 1
            else:
                anagram_map_s[string] += 1
        
        for x in t:
            if x not in anagram_map_t:
                anagram_map_t[x] = 1
            else:
                anagram_map_t[x] += 1
        
        if anagram_map_s == anagram_map_t:
            return True
        else:
            return False
