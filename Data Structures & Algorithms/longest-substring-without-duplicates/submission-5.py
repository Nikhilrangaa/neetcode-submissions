class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        new_set = set()
        l = 0
        res = 0

        for r in range(len(s)):
            while s[r] in new_set:
                new_set.remove(s[l])
                l += 1
            new_set.add(s[r])
            res = max(res, r - l + 1)
        
        return res








        