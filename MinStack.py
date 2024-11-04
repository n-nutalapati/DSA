class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, x):
        self.stack.append(x)

        if self.minStack:
            if x < self.min[-1]:
                self.minStack.append(x)
        else:
            self.minStack.append(x)

    def pop(self):
        if self.stack [-1] == self.minStack[-1]:
            self.minStack.pop()

        self.stack.pop()  

    def top(self):
        return self.stack[-1]
    
    def getMin(self):
        return self.minStack[-1]