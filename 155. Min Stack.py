class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.minstack=[]
    
    def push(self, x: int) -> None:
        if not self.minstack:
            self.minstack.append((x,x))
            return
        current_min=self.minstack[-1][1]
        self.minstack.append((x,min(x,current_min)))
        
        
    def pop(self) -> None:
        if not self.minstack:
            return None
        else:
            return self.minstack.pop()
            
    def top(self) -> int:
        top=self.minstack[-1][0]
        return top 

    def getMin(self) -> int:
        if not self.minstack:
            return None
        else:
            return self.minstack[-1][1]
        
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
