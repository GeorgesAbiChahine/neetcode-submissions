class MinStack:
    
    def __init__(self):
        self.stack = []
        self.size = 0        

        

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.size += 1
 
        

    def pop(self) -> None:
        if (self.size == 0):
            return
        self.stack.pop()
        self.size -= 1
            
        

    def top(self) -> int:
        if (self.size == 0):
            return -1
        return self.stack[self.size - 1]    
        

    def getMin(self) -> int:
        if (self.size == 0):
            return -1
        min = self.top()      
        for i in range(self.size):
            if (self.stack[i] < min):
                min = self.stack[i]
        return min

        
