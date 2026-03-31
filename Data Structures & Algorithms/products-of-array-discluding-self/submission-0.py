class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefArr = [0] * n
        suffArr = [0] * n
        i = 0
        while i < n:
            # Each index of nums = index of pref/suff Arr
            # Add itself to the previous prefix/suffix.
            if i != 0:
                prefArr[i] = nums[i-1] * prefArr[i-1]
            else:
                prefArr[i] = 1
            
            i+=1
        
        for j in range(n-1, -1, -1):
            print(j)
            if j != n-1:
                suffArr[j] = suffArr[j+1] * nums[j+1]
            else:

                suffArr[j] = 1
        
        finalArr=[0] * n
        print(suffArr)
        print(prefArr)
        for i in range(0, n):
            finalArr[i] = prefArr[i] * suffArr[i]
        
        return finalArr