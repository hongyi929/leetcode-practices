class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Nested list with 9 nested arrays
        # To count row and column duplicate, i could have 2 dictionaries 1 for row and 1 for col
        # Or what if I used the same dict, and stored another dict inside that dict.
        # O(1) lookup.
        # Key could be rowno or colno
        # I could store a number, and have an array with [row, col, sub-box from 1-9]
        # If the number matches immediately return false, e.g. 1 is in row 1 col 1 subbox 1
        # another no is row 2 col 2 subbox 1
        # check if array exists in the dict, else append to nested array.
        # but thats a very long runtime, every number has its own array created within the dictionary
        # Use key to check for duplc. value is a dummy value
        occurDict = {}
        for rn in range(0,9):
            for cn in range(0,9):
                num = board[rn][cn]
                if num == ".":
                    continue
                subbox = -1
                # subbox checker
                if rn < 3:
                    if cn == 0 or cn == 1 or cn == 2:
                        subbox = 0
                    elif cn == 3 or cn == 4 or cn == 5:
                        subbox = 1
                    else:
                        subbox = 2
                elif rn < 6:
                    if cn == 0 or cn == 1 or cn == 2:
                        subbox = 3
                    elif cn == 3 or cn == 4 or cn == 5:
                        subbox = 4
                    else:
                        subbox = 5

                else:
                    if cn == 0 or cn == 1 or cn == 2:
                        subbox = 6
                    elif cn == 3 or cn == 4 or cn == 5:
                        subbox = 7
                    else:
                        subbox = 8
                
                if occurDict.get(num) == None:
                    occurDict[num] = {
                        "row": [rn],
                        "column": [cn],
                        "subbox": [subbox]
                    }
                else:
                    for i in occurDict[num]["row"]:
                        if i == rn:
                            return False
                    for i in occurDict[num]["column"]:
                        if i == cn:
                            return False
                    for i in occurDict[num]["subbox"]:
                        if i == subbox:
                            return False

                    occurDict[num]["row"].append(rn)
                    occurDict[num]["column"].append(cn)
                    occurDict[num]["subbox"].append(subbox)


                #positionArr = [num, rn, cn, subbox]
                #if occurDict.get(str(positionArr)) == None:
                #    occurDict[str(positionArr)] = 1
                #else:
                #    return False
        return True

            
        