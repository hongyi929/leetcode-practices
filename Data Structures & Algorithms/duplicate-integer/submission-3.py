class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if len(nums) == 0:
            return False
        maxx = max(nums)
        minn = min(nums)
        
        if minn > 0: 
            countArr = [0] * (maxx + 1)
        else:
            if maxx < 0:
                countArr = [0] * ((-minn) + 1)
            else:
                countArr = [0] * (maxx + 1 + -(minn))
        for num in nums:
            countArr[num] += 1
        for count in countArr:
            if count > 1:
                return True
        return False