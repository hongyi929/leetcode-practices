class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        maxFreq = 0
        maxChar = ""
        l = 0
        i = 0
        r = 0
        length = 0
        maxLength = 0
        occurMap = {}
        # Valid case: If sliding window is valid, if rplcChar <= k , means I can replace all
        # and the substring is possible as a longest string. 
        # If invalid, I reduce the size and scope of the string
        # Allowing me to go through all possilbe substrings in a contiguous form
        # Every time a valid case is met the possibility just increases in size
        
        while r < n:
            if occurMap.get(s[r]) == None:
                occurMap[s[r]] = 1
            else:
                occurMap[s[r]] += 1
            
            length = (r-l) + 1
            if occurMap[s[r]] > maxFreq:
                maxChar = s[r]
                maxFreq = occurMap[s[r]]
            
            if length-maxFreq <= k:
                r+=1
                if length > maxLength:
                    print(length, " replaced")
                    maxLength = length
                
            else:
                occurMap[s[l]] -= 1
                l += 1
                occurMap[s[r]] -=1
            
        return maxLength


            