import sys
from collections import deque

class Queue:
    def __init__(self):
        self.items = deque([])
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        if self.empty():
            return -1
        return self.items.popleft()
    
    def size(self):
        return len(self.items)
    
    def empty(self):
        return int(self.items == deque([]))
    
    def back(self):
        if self.empty():
            return -1
        return self.items[-1]
    
    def front(self):
        if self.empty():
            return -1
        return self.items[0]
    

num_commands = int(sys.stdin.readline().rstrip())
queue = Queue()

for _  in range(num_commands) :
    command = sys.stdin.readline().rstrip().split()
    
    if command[0] == 'push':
        queue.push(int(command[1]))
        
    elif command[0] == 'pop':
        print(queue.pop())
        
    elif command[0] == 'size':
        print(queue.size())
        
    elif command[0] == 'empty':
        print(queue.empty())
    
    elif command[0] == 'back':
        print(queue.back())
        
    elif command[0] == 'front':
        print(queue.front())
    else :
        print(f'{command[0]} Invalid command')
        
    

