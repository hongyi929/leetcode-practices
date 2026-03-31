class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefArr = [0] * n
        i = 0
        while i < n:
            if i != 0:
                prefArr[i] = nums[i-1] * prefArr[i-1]
            else:
                prefArr[i] = 1
            i+=1
        
        for j in range(n-1, -1, -1):
            
            if j != n-1:
                suffix = suffix * nums[j+1]
            else:
                suffix = 1
            prefArr[j] = suffix * prefArr[j]

        
        
        return prefArr