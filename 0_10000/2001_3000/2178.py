from sys import stdin
from collections import deque

d = [[1, 0], [-1, 0], [0, 1], [0, -1]]

input = stdin.readline

row, col = map(int, input().split())

maze = []
for _ in range(row):
    maze.append(list(map(int, input().rstrip())))


q = deque([(0, 0)])
target = (row - 1, col - 1)
visited = set()
step = 0

while q:
    q_size = len(q)
    step += 1
    for _ in range(q_size):
        
        pt = q.popleft()
        if pt == target:
            print(step)
            exit(0)

        for dx, dy in d:
            tmp_pt = (pt[0] + dx, pt[1] + dy) 
            if 0 <= tmp_pt[0] < row and 0 <= tmp_pt[1] < col and maze[tmp_pt[0]][tmp_pt[1]] and tmp_pt not in visited:
                visited.add(tmp_pt)
                q.append(tmp_pt)




