class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # Stack: Monotonic stack keeping track of increasing heights.
        # On meeting a decreasing height, pop until no longer less.
        # This calculates all possible rectangle areas:
            # If popped, calcuates possible largest area for that height.
            # If not popped, continues till it calculates the largest area for that
            # bar height
        
        maxArea = 0
        stack = []
        newIndexArr = []
        area = 0
        n = len(heights)

        # Loop to iterate through array
        for i in range(n):
            # Add to stack if less than or not-existing
            if len(stack) == 0 or heights[i] >= stack[-1][1]:
                stack.append([i, heights[i]])
            else:
                while len(stack) > 0:
                    if stack[-1][1] > heights[i]:
                        area = stack[-1][1] * (i - stack[-1][0])
                        print(area)
                        newIndex = stack.pop()
                    if len(stack) == 0 or stack[-1][1] <= heights[i]:
                        stack.append([newIndex[0], heights[i]])
                        print("hi")
                        if area > maxArea:
                            maxArea = area
                        break
                    if area > maxArea:
                        maxArea = area
        
        print(stack)
        for i in stack:
            area = i[1] * (n-i[0])
            if area > maxArea:
                maxArea = area
         
        return maxArea

