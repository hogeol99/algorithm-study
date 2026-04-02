hour, minute = map(int,input().split())

need_time = int(input())

time = hour*60 + minute

time = ( time + need_time ) %(60*24)

print(time//60 , time % 60)