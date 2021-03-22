##Stack
class Stack(object):
    def __init__(self):
        self.items=[]
    def is_empty(self):
        return len(self.items)==0
    def push(self,item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def peek(self):
        return self.items[-1]
    def size(self):
        return len(self.items)
    def __str__(self):
        return str(self.items)

if __name__ == "__main__":
    stack=Stack()
    print(stack)
    print(stack.is_empty())
    stack.push(10)
    stack.push(16)
    stack.push(1)
    stack.push(13)
    stack.push(14)
    print(stack)
    print(stack.size())
    stack.pop()
    print(stack)
    print(stack.peek())
    print(stack.size())
