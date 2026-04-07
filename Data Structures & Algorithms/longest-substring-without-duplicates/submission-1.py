class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = 0
        maxLength = 0
        length = 0
        hashMap = {}
        while r < len(s):
            # if valid vs invalid aka detect duplicate
            if hashMap.get(s[r]) == None:
                print(r)
                length += 1
                hashMap[s[r]] = 1
                r += 1
            else:
                if s[r] != s[l]:
                    
                    del hashMap[s[l]]
                    l+=1
                else:
                    if length > maxLength:
                        maxLength = length
                    l += 1
                    length = (r-l) + 1
                    r +=1
        if length > maxLength:
            maxLength = length
            
        return maxLength