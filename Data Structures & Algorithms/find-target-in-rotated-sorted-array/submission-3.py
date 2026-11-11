class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            
            #left half

            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1 # target in left half
                else:
                    left = mid + 1 # target in right half 
            
            #right half 
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1 #target in right half
                else:
                    right = mid - 1
            
        return -1 


        