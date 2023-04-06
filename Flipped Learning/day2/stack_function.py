import sys

num_commands = int(sys.stdin.readline().rstrip())
stack = []

for _  in range(num_commands) :
    command = sys.stdin.readline().rstrip().split()
    
    if command[0] == 'push':
        stack.append(int(command[1]))
        
    elif command[0] == 'pop':
        if stack == []:
            print(-1)
        else:
            print(stack.pop())
        
    elif command[0] == 'size':
        print(len(stack))
        
    elif command[0] == 'empty':
        print(int(stack == []))
    
    elif command[0] == 'top':
        if stack == []:
            print(-1)
        else:
            print(stack[-1])
    
    else :
        print(f'{command[0]} Invalid command')
        
    

