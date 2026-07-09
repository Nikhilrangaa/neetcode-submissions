class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        duplicate_map = {}
        for x in nums:
            if x in duplicate_map:
                duplicate_map[x] += 1
                return True
            else:
                duplicate_map[x] = 1
        return False
        

        

        

            

        

        