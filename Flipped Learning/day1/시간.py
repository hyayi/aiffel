import sys 
wake_up_time = list(map(int,sys.stdin.readline().split()))
total_minute = wake_up_time[0]*60 + wake_up_time[1]
alarm_time = total_minute  - 45
alarm_house = alarm_time//60 if alarm_time//60 >= 0 else 24 + alarm_time//60
alarm_minute = alarm_time%60
print(f'{alarm_house} {alarm_minute}')