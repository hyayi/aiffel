import sys
from collections import deque

num_commands = int(sys.stdin.readline().rstrip())
stack = deque([])

for _  in range(num_commands) :
    command = sys.stdin.readline().rstrip().split()
    
    if command[0] == 'push':
        stack.append(int(command[1]))
        
    elif command[0] == 'pop':
        if stack == deque([]):
            print(-1)
        else:
            print(stack.popleft())
        
    elif command[0] == 'size':
        print(len(stack))
        
    elif command[0] == 'empty':
        print(int(stack == deque([])))
    
    elif command[0] == 'front':
        if stack == deque([]):
            print(-1)
        else:
            print(stack[0])
            
    elif command[0] == 'back':
        if stack == deque([]):
            print(-1)
        else:
            print(stack[-1])
    
    else :
        print(f'{command[0]} Invalid command')
        
    

