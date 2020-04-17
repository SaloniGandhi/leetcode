class MaxStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.maxstack=[]

    def push(self, x: int) -> None:
         if not self.maxstack:
            self.maxstack.append((x,x))
            return
         else:
            currentmax=self.maxstack[-1][1]
            self.maxstack.append((x,max(x,currentmax)))

    def pop(self) -> int:
        return self.maxstack.pop()[0]
         

    def top(self) -> int:
        return self.maxstack[-1][0]
        

    def peekMax(self) -> int:
        return self.maxstack[-1][1]
        

    def popMax(self) -> int:
        #basically pop max and return the stack
        maxsofar=self.maxstack[-1][1]
        b=[]
        while(maxsofar != self.maxstack[-1][0]):
            b.append(self.maxstack.pop())
        self.maxstack.pop()
        #self.maxstack.extend(reversed(b))
        for item in reversed(b):
            self.push(item[0])
        #map(self.push, reversed(b))
        
        return maxsofar
        


# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()
