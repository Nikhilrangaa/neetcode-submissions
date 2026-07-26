class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        anagram_map_s = {}
        anagram_map_t = {}

        proper_s = sorted(s)
        proper_t = sorted(t)

        if proper_s != proper_t:
            return False
        else:
            return True


        