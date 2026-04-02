hour, minute = map(int,input().split())

time = hour*60 + minute

time = ( time - 45 ) %(60*24)

print(time//60 , time % 60)