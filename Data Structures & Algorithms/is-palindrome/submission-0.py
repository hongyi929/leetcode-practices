class Solution:
    def isPalindrome(self, s: str) -> bool:
        # turn lowercase
        # remove non-alphanumeric

        # hashmap can count occurrence of letters. or a stack.
        # wait yea, use a stack. fifo
        # everything gets added to the stack, and then removed from the beginning
        
        s2 = ""
        s = "".join(filter(str.isalnum, s)).lower() # filter returns a filter object
        s2 = s
        n = len(s)
        for i in range(0, n):
            
            letter = s[n - 1 - i]
            if letter != s2[i]:
                return False

        
        return True
        
