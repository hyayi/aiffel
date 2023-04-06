import sys 
while True:
    numbers = sys.stdin.readline().rstrip()
    if numbers == '0':
        break
    elif numbers == numbers[::-1]:
        print('yes')
    else :
        print('no')