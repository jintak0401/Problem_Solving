from sys import stdin

input = stdin.readline
inf = float('inf')

def get_min(arr, x, y):
    
    ret_val = inf
    for i in range(5):
        ret_val = min(ret_val, arr[x][i] + get_force(i, y))
        ret_val = min(ret_val, arr[i][y] + get_force(i, x))
    return ret_val

def get_force(a, b):
    if a == 0:
        return 2

    elif b == 0:
        return inf

    elif a == b:
        return 1

    elif abs(a - b) == 2:
        return 4

    else:
        return 3

def init(arr, n):
    for i in range(5):
        arr[n][i] = inf
        arr[i][n] = inf

def solve(arr):
    
    move = [[[inf] * 5 for _ in range(5)] for _ in range(2)]

    move[0][0][arr[0]] = 2
    move[0][arr[0]][0] = 2

    seq = 1

    for i in range(1, len(arr)):

        for j in range(5):
            move[seq][j][arr[i]] = get_min(move[seq ^ 1], j, arr[i])
            move[seq][arr[i]][j] = move[seq][j][arr[i]]

        init(move[seq ^ 1], arr[i - 1])
        seq ^= 1


    return min(move[seq ^ 1][arr[-1]])

arr = [*map(int, input().split())]
ans = solve(arr[:-1])
print(ans)


