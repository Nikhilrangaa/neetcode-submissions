class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        newSet = set(nums)
        longest = 0

        for n in nums:
            if (n -1) not in newSet:
                length = 0
                
                while (n + length) in newSet:
                    length += 1

                longest = max(longest, length)

        return longest
