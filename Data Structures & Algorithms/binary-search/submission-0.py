class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        l = 0
        r = n - 1

        while l <= r:
            m = (r + l) // 2
            if nums[m] == target:
                return m
            elif target > nums[m]:
                l = m + 1
            elif target < nums[m]:
                r = m - 1
        
        return -1
