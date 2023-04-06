import sys 
number1 = sys.stdin.readline().rstrip()
number2 = sys.stdin.readline().rstrip()

for num in range(0, len(number1)):
    print(int(number2*num))
print(int(number1)*int(number2))