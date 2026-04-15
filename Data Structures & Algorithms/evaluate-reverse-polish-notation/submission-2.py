class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # Numbers precede their operations
        # Number: Add to stack. 
        # Operation: Remove 2 numbers?
        operationMap = {
            "+" : "+",
            "-" : "-",
            "*" : "*",
            "/" : "/"
        }
        stack = []
        for operand in tokens:
            if operand not in operationMap:
                stack.append(int(operand))
            else:
                rightNumber = stack.pop()
                leftNumber = stack.pop()
                result = 0
                if operand == "+":
                    result = leftNumber + rightNumber
                elif operand == "-":
                    result = leftNumber - rightNumber
                elif operand == "*":
                    result = leftNumber * rightNumber
                else:
                    result = int(leftNumber / rightNumber)
                stack.append(result)
                print(leftNumber, operand, rightNumber)
        return stack[0]
                
