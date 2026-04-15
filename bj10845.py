import sys

input = sys.stdin.readline


n = int(input())
queue = []
for i in range(n):
    commands = input().split()
    if commands[0] == "push":
        queue.append(commands[1])
    elif commands[0] == "pop":
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])
            queue.remove(queue[0])
    elif commands[0] == "size":
        print(len(queue))
    elif commands[0] == "empty":
        if len(queue) == 0:
            print(1)
        else:
            print(0)

    elif commands[0] == "front":
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])
    elif commands[0] == "back":
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[-1])        
           