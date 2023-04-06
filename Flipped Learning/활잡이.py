import sys
my_input =  sys.stdin.readline

inputs = int(my_input())
mountains = list(map(int, my_input().rstrip().split()))

max_attact = 0
i = 0
while True:
    attact = 0
    for j in range(i+1, len(mountains)):
        if mountains[i] > mountains[j]:
            attact += 1
        else:
            i = j
            break
    if attact > max_attact:
        max_attact = attact

print(max_attact)