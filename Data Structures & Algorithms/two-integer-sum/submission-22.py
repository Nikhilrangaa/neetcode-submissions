class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        hashmap = {}

        for i, number in enumerate(nums):
            hashmap[number] = i
        
        for i, number in enumerate(hashmap):
            complement = target - number
            if complement in hashmap and i != hashmap[complement]:
                return [i, hashmap[complement]]
            
        
        



        