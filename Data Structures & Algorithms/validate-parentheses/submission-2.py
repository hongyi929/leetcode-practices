class Solution:
    def isValid(self, s: str) -> bool:
        bracketPairs = {
            '(' : ")",
            "{" : "}",
            "[" : "]"
        }

        stringArr = []
        for bracket in s:
            # I want to add if its an opening bracket, check for pop if its not
            if bracket in bracketPairs:
                stringArr.append(bracket)
            else:
                if len(stringArr) == 0:
                    return False
                popBracket = stringArr.pop()
                if bracketPairs[popBracket] != bracket:
                    return False

        if len(stringArr) > 0:
            return False

        return True