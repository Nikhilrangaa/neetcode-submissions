class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            index = (right + left) // 2
            if nums[index] == target:
                return index
            if nums[index] < target:
                left = index + 1
            if nums[index] > target:
                right = index - 1
        return -1



        