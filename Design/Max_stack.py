class MaxStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.primary=[]
        self.secondary=[]
        

    def push(self, x: int) -> None:
        self.primary.append(x)
        if len(self.secondary)==0:
            self.secondary.append(x)
        else:
            maxi=max(x,self.secondary[-1])
            self.secondary.append(maxi)
        

    def pop(self) -> int:
        if len(self.primary)!=0:
            val=self.primary.pop()
            self.secondary.pop()
        return val

    def top(self) -> int:
        if len(self.primary)!=0:
            return self.primary[-1]

    def peekMax(self) -> int:
        if len(self.secondary)!=0:
            return self.secondary[-1]

    def popMax(self) -> int:
        stack1=[]
        maxele=self.peekMax()
        while self.top()!=maxele:
            stack1.append(self.pop())
        self.pop()
        while len(stack1)>0:
            self.push(stack1.pop())
        return maxele
            

# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()