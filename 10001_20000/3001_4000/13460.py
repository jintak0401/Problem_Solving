from sys import stdin
from collections import deque
from copy import deepcopy

board = []
case = deque([])    # [ red[x, y], blue[x, y], case_num, direction ]
converter = {'U' : [-1, 0], 'R' : [0, 1], 'D' : [1, 0], 'L' : [0, -1] }

def insert_case(case_num, blue, red, direction):
    global case, board

    if case_num == 11 or board[blue[0]][blue[1]] == 'O':
        return

    if (board[red[0] - 1][red[1]] == '.' or board[red[0] - 1][red[1]] == 'O' or board[blue[0] - 1][blue[1]] == '.') and direction != 'D':
        case.append([deepcopy(red), deepcopy(blue), case_num, 'U'])
    
    if (board[red[0]][red[1] + 1] == '.' or board[red[0]][red[1] + 1] == 'O' or board[blue[0]][blue[1] + 1] == '.') and direction != 'L':
        case.append([deepcopy(red), deepcopy(blue), case_num, 'R'])
    
    if (board[red[0] + 1][red[1]] == '.' or board[red[0] + 1][red[1]] == 'O' or board[blue[0] + 1][blue[1]] == '.') and direction != 'U':
        case.append([deepcopy(red), deepcopy(blue), case_num, 'D'])

    if (board[red[0]][red[1] - 1] == '.' or board[red[0]][red[1] - 1] == 'O' or board[blue[0]][blue[1] - 1] == '.') and direction != 'R':
        case.append([deepcopy(red), deepcopy(blue), case_num, 'L'])

def move_bead(red, blue, direction):
    
    first, second = red, blue
    if direction == 'U' and red[0] > blue[0]:
        first, second = second, first
    elif direction == 'R' and red[1] < blue[1]:
        first, second = second, first
    elif direction == 'D' and red[0] < blue[0] :
        first, second = second, first
    elif direction == 'L' and red[1] > blue[1]:
        first, second = second, first

    cv = converter[direction]
    ret_val = False

    while board[first[0]][first[1]] == '.':
        first[0] += cv[0]
        first[1] += cv[1]

    if board[first[0]][first[1]] == 'O':
        ret_val = True

    else:
        first[0] -= cv[0]
        first[1] -= cv[1]

    while board[second[0]][second[1]] == '.' and second != first:
        second[0] += cv[0]
        second[1] += cv[1]

    if board[second[0]][second[1]] == 'O':
        ret_val = True

    else:
        second[0] -= cv[0]
        second[1] -= cv[1]


    return ret_val


blue, red = [0, 0], [0, 0]
row, col = map(int, stdin.readline().split())
ans = -1

for i in range(row):
    board.append(list(stdin.readline()))

for i in range(1, len(board) - 1):
    for j in range(1, len(board[i]) - 1):
        if board[i][j] == 'R':
            red = [i, j]
            board[i][j] = '.'
        elif board[i][j] == 'B':
            blue = [i, j]
            board[i][j] = '.'



insert_case(1, blue, red, 'N')
# print('----------------------')
# print('red --> ', red)
# for i in case:
    # print(i)
# print('----------------------')

while len(case) > 0 :
    red, blue, case_num, direction = case.popleft()

    check = move_bead(red, blue, direction)
    
    if check:
        if board[blue[0]][blue[1]] == 'O':
            continue;
        else:
            ans = case_num
            break

    insert_case(case_num + 1, blue, red, direction)
    # print('----------------------')
    # print('red --> ', red)
    # for i in case:
        # print(i)
    # print('----------------------')



print(ans)

