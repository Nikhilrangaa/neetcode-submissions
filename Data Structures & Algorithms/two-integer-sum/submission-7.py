class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}

        for i, x in enumerate(nums):
            hash_map[x] = i
        
        for i, x in enumerate(nums):
            complement = target - nums[i]
            if complement in hash_map and hash_map[complement] != i:
                return [i, hash_map[complement]]