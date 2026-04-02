class Solution:
    def isPalindrome(self, s: str) -> bool:
        s2 = ""
        s = "".join(filter(str.isalnum, s)).lower() # filter returns a filter object
        s2 = s
        n = len(s)
        for i in range(0, n):
            letter = s[n - 1 - i]
            if letter != s2[i]:
                return False
        return True
        
