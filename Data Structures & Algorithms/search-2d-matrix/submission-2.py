class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        l = 0
        r = m-1
        # 1. How do u deal with non-existent but within matrix cases 
        # Should be the first check u perform
        if target > matrix[m-1][n-1]:
            return False
        
        if target < matrix[0][0]:
            return False    
        
        while l <= r:
            middle = l + (r-l) // 2
            if target == matrix[middle][0]:
                return True
            elif target > matrix[middle][0]:
                if target <= matrix[middle][n-1]:
                    for i in matrix[middle]:
                        if i == target:
                            return True
                    return False
                    # perform iteration through array
                    # 100% in this array
                # needs to break above so u can run the left-adder
                l = middle + 1
            else:
                r = middle - 1

        return False
