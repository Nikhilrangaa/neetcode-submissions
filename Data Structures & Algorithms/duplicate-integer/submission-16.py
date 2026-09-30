class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        new_set = set()
        for n in nums:
            new_set.add(n)
        
        if len(new_set) == len(nums):
            return False
        else:
            return True



        