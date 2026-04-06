class Solution:
    def trap(self, height: List[int]) -> int:

        n = len(height)
        suffix = [0] * n
        prefix = [0] * n
        largePref = 0
        largeSuff = 0
        i = 0
        maxArea = 0
        possArea = 0
        while i < n:
            if i == 0:
                largePref = height[0]
                largeSuff = height[n-1]
                i += 1
            else:
                if height[i] > largePref:
                    prefix[i] = largePref
                    largePref = height[i]
                else:
                    prefix[i] = largePref
                
                if height[n-1-i] > largeSuff:
                    suffix[n-1-i] = largeSuff
                    largeSuff = height[n-1-i]
                else:
                    suffix[n-1-i] = largeSuff
                
                i+=1
        
        i = 0
        print(prefix)
        print(suffix)
        while i < n:
            
            possArea = min(prefix[i], suffix[i]) - height[i]
            if possArea > 0:
                maxArea += possArea
            i += 1
        
        return maxArea
 


