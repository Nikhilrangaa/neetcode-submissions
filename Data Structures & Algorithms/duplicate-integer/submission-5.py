class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        duplicate_map = {}

        for number in nums:
            if number in duplicate_map:
                return True
            else:
                duplicate_map[number] = True
        return False

            

        