class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # Check for decreasing vs non-decreasing
        # On non-decreasing: Begin to pop from stack and count indice difference
        # After stack empty, add current element to indice stack and continue
        indiceStack = []
        finalStack = [0] * len(temperatures)
        i = 0
        while i < len(temperatures):
            if i == 0:
                indiceStack.append(i)
                i += 1
                continue
            
            if temperatures[i] <= temperatures[indiceStack[-1]]:
                indiceStack.append(i)
            else:
                while len(indiceStack) > 0:
                    if temperatures[i] <= temperatures[indiceStack[-1]]:
                        break
                    indice = indiceStack.pop()
                    finalStack[indice] = i - indice
                    
                indiceStack.append(i)
            
            i += 1
        
        for indice in indiceStack:
            finalStack[indice] = 0
        
        return finalStack



             