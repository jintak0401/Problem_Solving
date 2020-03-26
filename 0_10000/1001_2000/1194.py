from sys import stdin
from collections import deque


d = [[1, 0], [-1, 0], [0, 1], [0, -1]]
input = stdin.readline

row, col = map(int, input().split())

maze = []
check = True
for i in range(row): 
    
    user_input = list(input().rstrip())
    maze.append(user_input)
    if check:
        for j in range(len(user_input)):
            if user_input[j] == '0':
                check = False
                start_pt = (i, j)

q = deque([(start_pt, 0)])

visited = set([(start_pt, 0)])

step = 1

while q:

    q_size = len(q)

    for _ in range(q_size):

        pt, key = q.popleft()

        for dx, dy in d:
            x, y = pt[0] + dx, pt[1] + dy

            if 0 <= x < row and 0 <= y < col:
            
                if maze[x][y] == '#':
                    continue
                
                elif maze[x][y] == '1':
                    print(step)
                    exit(0)

                elif maze[x][y] == '0' or maze[x][y] == '.':
                    if ((x, y), key) not in visited:
                        visited.add(((x, y), key))
                        q.append(((x, y), key))

                elif ord('a') <= ord(maze[x][y]) <= ord('f'):
                    tmp_key = key | (1 << (ord(maze[x][y]) - ord('a')))
                    if ((x, y), tmp_key) not in visited:
                        visited.add(((x, y), tmp_key))
                        q.append(((x, y), tmp_key))

                elif ord('A') <= ord(maze[x][y]) <= ord('F'):
                    if key & (1 << (ord(maze[x][y]) - ord('A'))) and ((x, y), key) not in visited:
                        visited.add(((x, y), key))
                        q.append(((x, y), key))

    step += 1

print(-1)
