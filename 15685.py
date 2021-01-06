from collections import deque
from sys import stdin
from itertools import islice

board = [[0 for i in range(101)] for j in range(101)]
start_pt = []
generation = []
direction = []
converter = { 0 : 'R', 1 : 'U', 2 : 'L', 3 : 'D', 'R' : 'U', 'U' : 'L', 'L' : 'D', 'D' : 'R' }
ans = 0

def pointing_board(pt, d):
    global board

    if d == 'R':
        pt[1] += 1
    elif d == 'D':
        pt[0] += 1
    elif d == 'L':
        pt[1] -= 1
    elif d == 'U':
        pt[0] -= 1

    board[pt[0]][pt[1]] = 1

start_num = int(stdin.readline())

for i in range(start_num):
    x, y, d, g = map(int, stdin.readline().split())
    start_pt.append([y, x])
    generation.append(g)
    direction.append(converter[d])

for i in range(len(start_pt)):
    tmp = []
    pt = start_pt[i]
    d = direction[i]
    board[pt[0]][pt[1]] = 1
    pointing_board(pt, d)
    tmp.append(converter[d])
    for j in range(generation[i]):
        for k in range(len(tmp) - 1, -1, -1):
            pointing_board(pt, tmp[k])
            tmp.append(converter[tmp[k]])

    # print('=====================')
    # for i in range(7):
        # for j in range(7):
            # print(board[i][j], end = ' ')
        # print()
    # print('=====================')

for i in range(len(board) - 1):
    for j in range(len(board) - 1):
        if board[i][j] == 1 and board[i + 1][j] == 1 and board[i][j + 1] == 1 and board[i + 1][j + 1] == 1 :
            ans += 1

print(ans)
