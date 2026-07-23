class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        path = []

        def backtracking(i):
            if sum(path) == target:
                result.append(path.copy())
                return

            if sum(path) > target:
                return


            if i == len(nums):
                return
            
            path.append(nums[i])
            backtracking(i)

            path.pop()
            backtracking(i+1)
        
        backtracking(0)
        return result





    

        