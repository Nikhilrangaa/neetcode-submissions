class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
        product = 1

        for i in range(len(nums)):
            prefix.append(product)
            product *= nums[i]
        
        postfix = []
        product = 1

        for i in range(len(nums) - 1, -1, -1):
            postfix.append(product)
            product *= nums[i]
        
        postfix.reverse()
        
        result = [prefix[i] * postfix[i] for i in range(len(nums))]
        return result
        

        










        