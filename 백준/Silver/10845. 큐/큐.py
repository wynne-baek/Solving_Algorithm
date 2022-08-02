from collections import deque
import sys


def empty(queue):
    if queue:
        print(0)
    else:
        print(1)


def front(queue):
    if queue:
        print(queue[0])
    else:
        print(-1)


def back(queue):
    if queue:
        print(queue[-1])
    else:
        print(-1)


T = int(input())
queue = deque()
for i in range(T):
    command = list(sys.stdin.readline().split())
    if command[0] == 'push':
        x = int(command[1])
        queue.append(x)
    elif command[0] == 'pop':
        if queue:
            print(queue.popleft())
        else:
            print(-1)
    elif command[0] == 'size':
        print(len(queue))
    elif command[0] == 'empty':
        empty(queue)
    elif command[0] == 'front':
        front(queue)
    elif command[0] == 'back':
        back(queue)