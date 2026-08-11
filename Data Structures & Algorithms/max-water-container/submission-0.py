class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l,r = 0, len(heights) - 1
        maximum = 0

        while l < r:
            shorter_height = min(heights[l], heights[r])
            width = r - l
            area = shorter_height * width
            
            if area > maximum:
                maximum = area

            if heights[l] < heights[r]:
                l += 1
            elif heights[r] < heights[l]:
                r -= 1
            else:
                l += 1
        return maximum

        







        