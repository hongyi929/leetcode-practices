class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Hashmap to check occurrence as occurrence same = permutation
        # But checking occurrence is O(26) time on each iteration at its worst case.

        # Sliding window moves through valid/invalid cases. On adding a valid, occurrence must be added
        # and then match occurrence to continue. Have a 'match' counter to know when to break the loop
        # Invalid is when does not match occurrence

        # You need to check for a match occurrence on invalid: remove but added the same matching char.
        # I need a length checker to mitigate hidden non-match in the middle of the string
        s1Occur = {}
        s2Occur = {}
        matchCount = 0
        s1Length = len(s1)
        length = 0
        l = 0
        r = 0
        for char in s1:
            if s1Occur.get(char) == None:
                s1Occur[char] = 1
            else:
                s1Occur[char] += 1
        
        print(s1Occur)

        while r < len(s2):
            length = (r-l) + 1
            if length > s1Length:
                s2Occur[s2[l]] -= 1
                l += 1
                if s1Occur.get(s2[l-1]):
                    if matchCount > 0 and s1Occur.get(s2[l-1]) > s2Occur.get(s2[l-1]):
                        matchCount -= 1
                continue
            
            char = s2[r]
            if s2Occur.get(char) == None:
                s2Occur[char] = 1
            else:
                s2Occur[char] += 1
            
            # Check if character exists in string 1, thus can check string2's occurrence
            if s1Occur.get(char):
                if s2Occur[char] <= s1Occur[char]:
                    matchCount += 1
                else:
                    s2Occur[s2[l]] -= 1
                    l += 1
                    if s1Occur.get(s2[l-1]):
                        if matchCount > 0 and s1Occur.get(s2[l-1]) > s2Occur.get(s2[l-1]):
                            matchCount -= 1
                    
            else:
                # If it's not a match, you gotta remove that character.
                s2Occur[s2[l]] -= 1
                l += 1
                if s1Occur.get(s2[l-1]):
                        if matchCount > 0 and s1Occur.get(s2[l-1]) > s2Occur.get(s2[l-1]):
                            matchCount -= 1
            print(s2Occur)
            print(matchCount)
            if matchCount == s1Length:
                return True
                break
            r += 1
        return False
        
            