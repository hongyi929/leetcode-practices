class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        l = 0
        r = n-1
        lArea = 0
        area = 0
        while l < r:
            if heights[l] < heights[r]:
                area = heights[l] * (r-l)
                l +=1
            else:
                area = heights[r] * (r-l)
                r -=1
            if area > lArea:
                lArea = area
            


        
        return lArea 