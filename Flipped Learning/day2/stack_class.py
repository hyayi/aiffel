import sys

class Stack:
    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        if self.empty():
            return -1
        return self.items.pop()
    
    def size(self):
        return len(self.items)
    
    def empty(self):
        return int(self.items == [])
    
    def top(self):
        if self.empty():
            return -1
        return self.items[-1]
    

num_commands = int(sys.stdin.readline().rstrip())
stack = Stack()

for _  in range(num_commands) :
    command = sys.stdin.readline().rstrip().split()
    
    if command[0] == 'push':
        stack.push(int(command[1]))
        
    elif command[0] == 'pop':
        print(stack.pop())
        
    elif command[0] == 'size':
        print(stack.size())
        
    elif command[0] == 'empty':
        print(stack.empty())
    
    elif command[0] == 'top':
        print(stack.top())
    
    else :
        print(f'{command[0]} Invalid command')
        
    

