class MovingAverage:

    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.queue=[]
        self.front=-1
        self.rear=-1
        self.currentsize=0
        self.windowsize=size
        

    def next(self, val: int) -> float:
        #enqueue
        if self.currentsize==0:
            self.front=0
        self.rear+=1
        self.queue.append(val)
        self.currentsize+=1
        avg=0
        sum=0
        if self.currentsize>self.windowsize:
            self.front+=1
        #print(self.front)
        #print((self.queue[self.front:]))
        for i in (self.queue[self.front:]):
            sum+=i
        avg=sum/len(self.queue[self.front:])
        return avg
        
        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
