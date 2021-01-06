from sys import stdin
from collections import deque
from itertools import islice

# 2번 6번

gear = [0 for i in range(4)]

direction = {1 : -1, -1 : 1}

def rotate_gear(rotation, gear):
    # print(rotation)
    index = 0
    for i in rotation:
        if i == 0:
            pass
        elif i == 1:
            gear[index].appendleft(gear[index].pop())
        else :
            gear[index].append(gear[index].popleft())
        index += 1


for i in range(4):
    gear[i] = deque(list(map(int, list(input()))))

rotation = [0 for i in range(int(stdin.readline()))]

for i in range(len(rotation)):
    rotation[i] = list(map(int, stdin.readline().split()))
    rotation[i][0] -= 1

# print('====================')
# for i in gear:
    # print(i)
# print('====================')

for i in rotation:

    tmp = [0 for i in range(4)]
    tmp[i[0]] = i[1]

    for j in range(1, 4):
        if i[0] + j == 4:
            break

        elif gear[i[0] + j - 1][2] == gear[i[0] + j][6]:
            break
        
        else:
            tmp[i[0] + j] = direction[tmp[i[0] + j - 1]]

    for j in range(1, 4):
        if i[0] - j == -1:
            break

        elif gear[i[0] - j + 1][6] == gear[i[0] - j][2]:
            break
        
        else:
            tmp[i[0] - j] = direction[tmp[i[0] - j + 1]]

    rotate_gear(tmp, gear)
    # print('====================')
    # for i in gear:
        # print(i)
    # print('====================')

ans = 0


for i in range(len(gear)):
    if gear[i][0]:
        ans += 2 ** i

print(ans)
