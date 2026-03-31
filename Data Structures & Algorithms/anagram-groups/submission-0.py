class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Group by len, then count letters per group in len
        # loop through len -- O(n)
        # Loop through the sub-groups, 
        # To find an anagram, we used dictionary to count the occurrence
        # What if we stored the array of letters as the key
        # And the value is the actual word?
        # act --> [a,c,t] : 'act'
        # cat --> [a,c,t] : ['act', 'cat']
        stringDict = {

        }
        alphabetArr = [0] * 26
        for s in strs:
            for alp in s:
                alpIndex = ord(alp) - ord('a')
                alphabetArr[alpIndex] += 1
            alphabetArrStr = str(alphabetArr)
            if stringDict.get(alphabetArrStr) == None:
                stringDict[alphabetArrStr] = [s]
            else:
                stringDict[alphabetArrStr].append(s)
            
            alphabetArr = [0] * 26
        
        
        finalList = []
        for sublist in stringDict:
            finalList.append(stringDict[sublist])
        return finalList