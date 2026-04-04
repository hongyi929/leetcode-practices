class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        i = 0
        finalArr = []
        for num in nums:
            if i > 0 and nums[i] == nums[i-1]:
                i +=1
                continue
            
            l = i+1
            r = n-1
            neededSum = -nums[i]
            print(neededSum)

            while l < r:
                if neededSum == (nums[l] + nums[r]):
                    finalArr.append([nums[i], nums[l], nums[r]])
                    while l < r and nums[l] == nums[l+1]:
                        l +=1
                    while l < r and nums[r] == nums[r-1]:
                        r -=1
                    l += 1
                    r -= 1
                elif nums[l] + nums[r] > neededSum:
                    r -= 1
                else:
                    l += 1
            i +=1
        return finalArr