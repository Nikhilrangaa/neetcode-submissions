class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        newset = set(nums)
        longest = 0

        for n in nums:
            if (n - 1) not in newset:
                length = 0
                while (n + length) in newset:
                    length += 1
                longest = max(longest, length)
        
        return longest


            




        