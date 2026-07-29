class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}

        for i, num in enumerate(nums):
            map[num] = i
        
        for i, number in enumerate(map):
            complement = target - number
            if complement in map and i != map[complement]:
                return [i, map[complement]]

        


        




        