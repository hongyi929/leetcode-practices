class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:


        '''
        occurMap: Tracks occurrence of elements
        kArr: Tracks final top elements

        Process:
        1. Loops through nums array and logs occurrence in occurMap
        2. Loops through occurMap to log elements into kArr
        2.1: Add elements into kArr if kArr is not fully filled
        2.2: The loop for consecutive elements checks non-kArr elements with kArr elements
            If more occurrence, replace and loop ends to prevent duplicate.
        2.5: Checks if occurrence of candidate in kArr is less than new occurMap value
            If so, replace the old candidate with a new one.
        
        '''

        occurMap = {}
        kArr = []
        lowestCandidate = None
        for num in nums:
            if occurMap.get(num) == None:
                occurMap[num] = 1
            else:
                occurMap[num] += 1
        
        # I need to compare candidate occurrence to hashmap occurrence.
        for key in occurMap:
            if len(kArr) < k:
                kArr.append(key)
            else:
                top7Flag = False
                for candidate in kArr:

                    # Problem: No guarantee it replaces the worst of the current 7
                    # Leaving u with a non-top 7
                    # Solution: Identify the lowest of the current 7, and replace it

                    if occurMap[key] > occurMap[candidate]:
                        if lowestCandidate == None:
                            lowestCandidate = candidate
                            top7Flag = True
                        else:
                            if occurMap[lowestCandidate] > occurMap[candidate]:
                                lowestCandidate = candidate
                    
                if top7Flag:
                    print(lowestCandidate)
                    print(kArr)
                    kArr.remove(lowestCandidate)
                    kArr.append(key)
                    lowestCandidate = None
                    top7Flag = False
        return kArr
        