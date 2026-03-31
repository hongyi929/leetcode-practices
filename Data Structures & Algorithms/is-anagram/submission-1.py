class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        occurDict = {}

        for i in s:
            if occurDict.get(i) == None:
                occurDict[i] = 1
            else:
                occurDict[i] += 1
        
        for i in t:
            if occurDict.get(i) == None:
                return False
            else:
                occurDict[i] -= 1
                if occurDict[i] == 0:
                    del occurDict[i]
            
        if len(occurDict) == 0:
            return True
        else:
            return False