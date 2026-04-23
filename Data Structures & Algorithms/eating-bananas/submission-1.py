class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # Check more or less. On found, only binary search on less.
        n = len(piles)
        maxNo = 0
        minInt = None
        for p in piles:
            if p > maxNo:
                maxNo = p
        
        l = 1
        r = maxNo
        count = 0

        while l <= r:
            count = 0
            m = l + ((r-l) // 2)
            for p in piles:
                iterations = -(p // -m)
                count += iterations
            
            if count <= h:
                if not minInt:
                    minInt = m
                    
                if m < minInt:
                    minInt = m
                    
                r = m - 1
            else:
                l = m + 1

        return minInt
        
                


