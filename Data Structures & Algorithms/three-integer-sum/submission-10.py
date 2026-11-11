
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        # Sort the array to simplify duplicates and use 2 pointers
        nums.sort()
        res = []
        n = len(nums)

        # fix nums[i] and use left/right pointers to find pairs that sum to -nums[i]
        for i in range(n):
            if i> 0 and nums[i] == nums[i - 1]:
                continue
            left, right = i + 1, n - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total == 0:
                    res.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                elif total < 0:
                    left += 1
                else:
                    right -= 1
        return res
                


                    

        #Sort + 2 pointers 
        