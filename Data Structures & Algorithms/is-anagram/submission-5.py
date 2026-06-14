class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        anagram_map_s = {}
        anagram_map_t = {}
        for letter in s:
            if letter not in anagram_map_s:
                anagram_map_s[letter] = 1
            else:
                anagram_map_s[letter] += 1
        for letter in t:
            if letter not in anagram_map_t:
                anagram_map_t[letter] = 1
            else:
                anagram_map_t[letter] += 1
    
        if anagram_map_s == anagram_map_t:
            return True
        else:
            return False
        
        