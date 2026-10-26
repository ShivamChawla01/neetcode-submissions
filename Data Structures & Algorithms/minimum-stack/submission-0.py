class MinStack:

    def __init__(self):
        self.arr = []
        self.minimum = []
        

    def push(self, val: int) -> None:
        self.arr.append(val)
        if(len(self.minimum) > 0):
            temp = min(self.minimum[-1],val)
        else:
            temp = val
        self.minimum.append(temp)
        

    def pop(self) -> None:
        temp = self.arr[-1]
        del self.arr[-1]
        del self.minimum[-1]
        return temp

        

    def top(self) -> int:
        return self.arr[-1]
        

    def getMin(self) -> int:
        return self.minimum[-1]
        
