class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        track = {}

        for i,number in enumerate(nums):
            x = target - number
            if x in track:
                return [track[x], i]
            else:
                track[number] = i



        