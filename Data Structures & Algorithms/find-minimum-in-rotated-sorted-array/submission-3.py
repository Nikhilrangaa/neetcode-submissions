class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0]
        l, r = 0, len(nums) - 1

        while l <= r:
            middle = (l + r) // 2
            if nums[l] < nums[r]:
                return nums[l]
            elif nums[l] > nums[r]:
                if nums[l] < nums[middle]:
                    l = middle + 1
                elif nums[l] > nums[middle]:
                    r = middle
                elif nums[l] == nums[middle]:
                    l = middle + 1
            elif nums[l] == nums[r]:
                return nums[l]
                
                

                
            



                


        


            
        



        