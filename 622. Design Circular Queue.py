class MyCircularQueue:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        """
        self.k=k
        self.front=-1
        self.rear=-1
        self.size_current=0
        self.queue=[-1]*k
        
        

    def enQueue(self, value: int) -> bool:
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        """
        if self.isFull():
            return False
        if self.isEmpty():
            self.front=0
        self.rear=(self.rear+1)%self.k
        self.queue[self.rear]=value
        self.size_current+=1
        return True
        
        
        
        

    def deQueue(self) -> bool:
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        """
        if self.isEmpty():
            return False
        if self.rear==self.front:
            self.rear=-1
            self.front=-1
        else:
            self.front=(self.front+1)%self.k
        self.size_current-=1
        return True
            

            
        

    def Front(self) -> int:
        """
        Get the front item from the queue.
        """
        if self.isEmpty():
            return -1
        else:
            return self.queue[self.front]
        

    def Rear(self) -> int:
        """
        Get the last item from the queue.
        """
        if self.isEmpty():
            return -1
        return self.queue[self.rear]
        

    def isEmpty(self) -> bool:
        """
        Checks whether the circular queue is empty or not.
        """
        if self.size_current==0:
            return True
        

    def isFull(self) -> bool:
        """
        Checks whether the circular queue is full or not.
        """
        if self.size_current==self.k:
            return True


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
