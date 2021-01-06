from sys import stdin
from collections import deque
from itertools import permutations, product

inf = 10000000

def rotate(field, degree):
    if degree == 0:
        return field
    ret_val = [['0'] * 5 for _ in range(5)]
    for i in range(5):
        for j in range(5):
            if field[i][j] == '1':
                if degree == 1:
                    ret_val[j][4 - i] = '1'
                elif degree == 2:
                    ret_val[4 - i][4 - j] = '1'
                else:
                    ret_val[4 - j][i] = '1'

    return ret_val

def bfs(maze):

    if maze[0][0][0] == '0':
        return inf
    q = deque([(0, 0, 0)])
    d = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]
    visited = [[[False] * 5 for _ in range(5)] for _ in range(5)]
    step = 0
    while q:
        
        q_size = len(q)
        for _ in range(q_size):
            pos = q.popleft()
            if pos == (4, 4, 4):
                return step
            for dx, dy, dz in d:
                x, y, z = pos[0] + dx, pos[1] + dy, pos[2] + dz
                if 0 <= x < 5 and 0 <= y < 5 and 0 <= z < 5:
                    if maze[x][y][z] == '1' and not visited[x][y][z]:
                        q.append((x, y, z))
                        visited[x][y][z] = True
        step += 1
    return inf

def solve(maze):

    degree = list(product([0, 1, 2, 3], repeat=5))
    ans = inf
    for i in range(len(degree)):
        tmp_maze = [0] * 5
        for j in range(5):
            tmp_maze[j] = rotate(maze[j], degree[i][j])
        case = list(permutations(tmp_maze, 5))

        for j in range(len(case)):
            ans = min(ans, bfs(case[j])) 
            if ans == 12:
                return ans

    return ans
    


input = stdin.readline

maze = []

for _ in range(5):
    field = []
    for _ in range(5):
        field.append(input().split())
    maze.append(field)

ans = solve(maze)
print(ans if ans != inf else -1)
