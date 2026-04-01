class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Hashmap --> Lead to next integer. Then integer search for key. so on so forth
        # on iterating element A, put it in dict. If exist, make new key with extended list
        numMap = {}
        for num in nums:
            if numMap.get(num) == None:
                numMap[num] = 1
            else:
                continue
            
        gLength = 0
        length = 0
        for num in numMap:
            numFlag = False
            if numMap.get(num-1) == None:
                length = 1
                numFlag = True
                i = 1
                while numFlag:
                    if numMap.get(num+i) == None:
                        numFlag = False
                    else:
                        length += 1
                        i += 1
                        print(length)

                if length > gLength:
                    gLength = length
            else:
                continue
        return gLength