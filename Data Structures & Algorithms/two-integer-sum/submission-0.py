class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # I make a dictionary with the key as the difference, index as the number
        # Dictionary logging O(n) time complexity. But space complexity is O(n) too.
        sumDict = {}
        i = 0
        finalArr = []
        for num in nums:
            difference = target - num

            if sumDict.get(num) != None:
                finalArr.append(sumDict.get(num))
                finalArr.append(i)
                return finalArr

            if sumDict.get(difference) == None:
                sumDict[difference] = i
            


            i += 1