import sys
from collections import deque

class MyDeque:
    def __init__(self):
        self.items = deque([])
    
    def push_front(self, item):
        self.items.appendleft(item)
        
    def push_back (self, item):
        self.items.append(item)
        
    def pop_front(self):
        if self.empty():
            return -1
        return self.items.popleft()

    def pop_back(self):
        if self.empty():
            return -1
        return self.items.pop()
    
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
mydeque = MyDeque()

for _  in range(num_commands) :
    command = sys.stdin.readline().rstrip().split()
    
    if command[0] == 'push_front':
        mydeque.push_front(int(command[1]))
    
    elif command[0] == 'push_back':
        mydeque.push_back(int(command[1]))
        
    elif command[0] == 'pop_front':
        print(mydeque.pop_front())
        
    elif command[0] == 'pop_back':
        print(mydeque.pop_back())
    
    elif command[0] == 'size':
        print(mydeque.size())
    
    elif command[0] == 'empty':
        print(mydeque.empty())
    
    elif command[0] == 'back':
        print(mydeque.back())
    elif command[0] == 'front':
        
        print(mydeque.front())
    
    else :
        print(f'{command[0]} Invalid command')
        
    

