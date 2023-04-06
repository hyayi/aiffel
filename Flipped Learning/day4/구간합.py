## 구간합
import sys 

my_input =  sys.stdin.readline
n,m = my_input().rstrip().split()

num_list = list(map(int, my_input().rstrip().split()))
tmp_list = [0 for _ in range(int(n)+1)]

for i in range(1,len(num_list)+1) :
    tmp_list[i] = tmp_list[i-1]+num_list[i-1]
    
for _ in range(int(m)):
    start, end = map(int, my_input().rstrip().split())

    result  = tmp_list[end] - tmp_list[start-1]
    print(result)
    