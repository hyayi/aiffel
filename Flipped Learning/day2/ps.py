import sys 

def isvps(input_string):
    stack = []
    for i in range(0, len(input_string)):
        if input_string[i] == '(':
            stack.append('(')
        elif input_string[i] == ')':
            if stack == []:
                return 'NO'
            else:
                stack.pop()
    if stack == []:
        return 'YES'

iter_number = int(sys.stdin.readline().rstrip())

for _ in range(0, iter_number):
    input_string = sys.stdin.readline().rstrip()
    print(isvps(input_string))