class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        values = set()

        for num in nums:
            if num in values:
                return True
            if num not in values:
                values.add(num)
        return False


        