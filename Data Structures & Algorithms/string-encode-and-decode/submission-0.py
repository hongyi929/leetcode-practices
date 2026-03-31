class Solution:

    def encode(self, strs: List[str]) -> str:
        finalString = ""
        for string in strs:
            length = len(string)
            finalString += str(length) + "#" + string
        
        return finalString

    def decode(self, s: str) -> List[str]:
        # I need it to check every character.
        # Maybe a while loop, I can control when it stops.
        i = 0
        strLength = ""
        finalArr = []
        while i < len(s):
            if s[i] != "#":
                
                strLength += str(s[i])
                i += 1
            else:
                strLength = int(strLength)
                finalStr = s[i+1:i+strLength + 1]
                finalArr.append(finalStr)
                i += strLength + 1
                strLength = ""
        return finalArr


