class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0, len(heights) - 1
        max_area = 0

        # Loop untll the pointers meet
        while left < right:
            height = min(heights[left], heights[right])
            width = right - left
            area = height * width
            #update area
            max_area = max(max_area, area)
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        return max_area


        #Calcu.ate the current area

        # update

        
        