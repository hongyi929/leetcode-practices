class Solution:
    def findMin(self, nums: List[int]) -> int:
        # Three scenarios:
        # greater than l + r
        # greater than l but not r (l is the minimum)
        # smaller than l and r (not fully rotated, minimum is either itself or infront of it.)

        l = 0
        r = len(nums) - 1
        minInt = -1
        while l <= r:
            m = l + (r-l) // 2
            if nums[m] >= nums[l] and nums[m] >= nums[r]:
                l = m+1
                if minInt == -1 or nums[m] < minInt:
                    minInt = nums[m]
            elif nums[m] > nums[l] and nums[m] < nums[r]: # only works for first pass
                # afterwards this wont trigger again?
                return nums[l]
            else:
                r = m - 1
                if minInt == -1 or nums[m] < minInt:
                    minInt = nums[m]

        return minInt