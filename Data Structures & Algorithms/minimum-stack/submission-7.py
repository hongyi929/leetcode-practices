class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.minStack) == 0:
            current_min = val
            self.minStack.append(current_min)
        else:
            if val <= self.minStack[-1]:
                current_min = val
                self.minStack.append(current_min)
        

    def pop(self) -> None:
        if self.minStack[-1] == self.stack[-1]:
            self.minStack.pop()
        return self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        if not self.minStack:
            return
        return self.minStack[-1]
        
        # How do I get the minimum of the stack in O(1) time?
        # There must be a way to look it up.
        # Meaning, I need to find a way to store it, in either a hashtable or array.

        
