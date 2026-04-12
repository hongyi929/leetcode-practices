class Solution:
    def minWindow(self, s: str, t: str) -> str:
        tOccur = {}
        
        for alphabet in t:
            tOccur[alphabet] = tOccur.get(alphabet, 0) + 1

        totalMatches = 0
        finalStr = ""
        sOccur = {}
        l = 0
        r = 0
        
        # Not found: Increase R to extend sliding window 
        # Found: Increase matches
        # Complete Match: Shrink window (while loop while matches is still existing)
        # To not overcomplicate, only shrink on match (that's when the finalStr and L matters)
        while r < len(s):
            if not s or not t:
                return ""

            if s[r] not in tOccur:
                r += 1
                continue

            else:
                sOccur[s[r]] = sOccur.get(s[r], 0) + 1
                if sOccur[s[r]] == tOccur[s[r]]:
                    totalMatches += 1
            
            while totalMatches == len(tOccur):
                if s[l] in tOccur:
                    # Get rid of it in the window, but track it in the newStr.
                    if sOccur[s[l]] == tOccur[s[l]]:
                        sOccur[s[l]] -= 1
                        totalMatches -= 1
                    else:
                        sOccur[s[l]] -= 1
                
                l += 1

                if totalMatches != len(tOccur):
                    newStr = s[l-1:r+1]
                    if finalStr == "":
                        finalStr = newStr
                    elif len(finalStr) > len(newStr):
                        finalStr = newStr

            r += 1
        
        return finalStr

