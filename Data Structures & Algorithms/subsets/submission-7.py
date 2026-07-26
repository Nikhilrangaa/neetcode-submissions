class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        path = []

        def backtracking(i):
            if i == len(nums):
                result.append(path.copy())
                return
            
            path.append(nums[i])
            backtracking(i+1)

            path.pop()
            backtracking(i+1)
        
        backtracking(0)
        return result