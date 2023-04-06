import sys 
for _ in range(0, 3):
    total_value = 0
    iter_number = int(sys.stdin.readline())
    
    for _ in range(0, iter_number):
        sum_value = int(sys.stdin.readline())
        total_value += sum_value
        
    if total_value == 0:
        print("0")
    elif total_value > 0:
        print("+")
    elif total_value < 0:
        print("-")     
