import sys 

input = sys.stdin.readline

def return_cycle_number(number):
    iter_number = 0
    previous_number = number
    while True :
        iter_number += 1
        next_number =  ((previous_number // 10) + (previous_number % 10))%10 + (previous_number % 10)*10 
        if next_number == number:
            return iter_number
        previous_number = next_number

number = int(input().rstrip())
print(return_cycle_number(number))
