class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = [0]
        newArr = [0] * len(position)
        for i in range(len(position)):
            newArr[i] = [position[i], speed[i]]
        newArr.sort(reverse=True)

        for item in newArr:
            time = (target - item[0]) / item[1]
            if time > stack[-1]:
                stack.append(time)
            else:
                continue

        return len(stack) - 1        