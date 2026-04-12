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







        

                

                
        


'''
# Find until matching occurrence. Then remove until u reach matched char
        # Continue finding until you find next matching char. Remove until found matching char
        # On every reached match string, use if condition to replace length.

        l = 0
        r = 0
        matches = 0
        sOccur = {}
        tOccur = {}
        matchComplete = False
        finalStr = ""
        newStr = ""
        
        for alph in t:
            if tOccur.get(alph) == None:
                tOccur[alph] = 1
            else:
                tOccur[alph] += 1

        # Separate before and after functionality for clarity in code

        ## Before Matched String 

        while r < len(s):
            if not matchComplete:
                if sOccur.get(s[r]) == None:
                    sOccur[s[r]] = 1
                else:
                    sOccur[s[r]] += 1

                if not tOccur.get(s[r]):
                    r += 1
                else:
                    matches += 1
                    r += 1
                    if matches == len(t):
                        # I need to remmove behind occurrences
                        finalStr = s[l:r]
                        for char in finalStr:
                            if not tOccur.get(char):
                                l += 1
                                finalStr[l:r]
                            else:
                                break
                        matchComplete = True
            else:
                # But if you detect a new matched char, you may remove another one which ends up with a non-matched string.
                # I have to move to the 'shorter strings' route... Move Left to continue.
                if sOccur.get(s[r]) == None:
                    sOccur[s[r]] = 1
                else:
                    sOccur[s[r]] += 1
                
                if tOccur.get(s[r]) == None:
                    if tOccur.get(s[l]):
                        matches -= 1
                        sOccur[s[l]] -= 1
                        
                    l += 1
                    r += 1
                else:
                    # check for valid match
                    if tOccur[s[r]] == sOccur[s[r]]:
                        matches += 1

                        newStr = s[l:r+1]
                        for char in newStr:
                            if not tOccur.get(char):
                                l += 1
                                finalStr[l:]
                            else:
                                r += 1
                                break
                        
                        if len(newStr) < len(finalStr):
                            finalStr = newStr
                    else:
                        matches -= 1
                        sOccur[s[l]] -= 1
                        l += 1
                    
                    # fix this code full, then learn the optimized code

                    
        return finalStr
'''