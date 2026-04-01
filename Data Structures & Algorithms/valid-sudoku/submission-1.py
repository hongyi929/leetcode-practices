class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
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

            
        