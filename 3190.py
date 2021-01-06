import sys
from collections import deque
from itertools import islice

apple = []
move = []
size = 0
body = deque([[0, 0]])
direction = 'R'

ans = 0

def change_direction(change):

    global direction 

    if change == 'D':
        if direction == 'R':
            direction = 'D'
        elif direction == 'D':
            direction = 'L'
        elif direction == 'L':
            direction = 'U'
        else:
            direction = 'R'

    else:
        if direction == 'R':
            direction = 'U'
        elif direction == 'D':
            direction = 'R'
        elif direction == 'L':
            direction = 'D'
        else:
            direction = 'L'

def move_body():

    global body
    global apple
    global ans

    # print('%2d) body : '%(ans - 1), body)

    head = [body[-1][0], body[-1][1]]
    if direction == 'U':
        head[0] -= 1
    elif direction == 'R':
        head[1] += 1
    elif direction == 'D':
        head[0] += 1
    else:
        head[1] -= 1

    body.append(head)

    if head in islice(body, 0, len(body) - 1):
        print(ans)
        exit(0)

    elif head not in apple:
        body.popleft() 
    
    else:
        apple.remove(head)


size = int(sys.stdin.readline())
apple_len = int(sys.stdin.readline())

for i in range(apple_len):
    apple.append(list(map(int, sys.stdin.readline().split())))
    apple[-1][0] -= 1
    apple[-1][1] -= 1

move_len = int(sys.stdin.readline())

for i in range(move_len):
    tmp = sys.stdin.readline().split()
    move.append([int(tmp[0]), tmp[1]])

index = 0

while(True):

    ans += 1

    move_body()
    head = body[-1]

    if not (0 <= head[0] < size and 0 <= head[1] < size):
        # print(body)
        break
    
    elif body[-1] in list(islice(body, 0, len(body) - 1)):
        # print(body)
        break;

    if index < len(move) and ans == move[index][0]:
        change_direction(move[index][1])
        index += 1
    

print(ans)



