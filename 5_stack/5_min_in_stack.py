class Stack:
    def __init__(self):
        self.items = []
        self.min = None

    def push(self, item):
        self.items.append(item)
        self.minimun()

    def pop(self):
        if self.isEmpty():
            raise ValueError("Empty Stack")
        else:
            return self.items.pop()

    def minimun(self):
        if self.min is None:
            self.min = self.peek()
        else:
            if self.peek() < self.min:
                self.min = self.peek()

    def getMinimum(self):
        return self.min

    def peek(self):
        try:
            return self.items[-1]
        except IndexError as e:
            print(e)

    def size(self):
        return len(self.items)

    def isEmpty(self):
        return self.size() == 0

stack = Stack()
ele = [2,3,4,5,6,1]
for i in ele:
    stack.push(i)

print(stack.getMinimum()) 
    