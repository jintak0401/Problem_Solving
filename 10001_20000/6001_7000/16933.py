from sys import stdin
from collections import deque

def solve(arr, crash):
    
    d = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    inf = float('inf')
    dist = [[[inf for _ in range(crash + 1)] for _ in range(len(arr[0]))] for _ in range(len(arr))]
    dist[0][0][0] = 1
    q = deque([(0, 0, 0, 1, 1)])   # x, y, k, dist, is_day
    target = (len(arr) - 1, len(arr[0]) - 1)

    while q:
        
        x, y, k, t, is_day = q.popleft()

        if dist[x][y][k] != t or (x, y) == target:
            continue

        for dx, dy in d:
            nx, ny = x + dx, y + dy

            if 0 <= nx < len(arr) and 0 <= ny < len(arr[0]):

                if arr[nx][ny] == '0' and dist[nx][ny][k] > t + 1:
                    q.append((nx, ny, k, t + 1, is_day ^ 1))
                    dist[nx][ny][k] = t + 1

                elif arr[nx][ny] == '1' and k < crash:
                    if is_day == 1 and dist[nx][ny][k + 1] > t + 1:
                        q.append((nx, ny, k + 1, t + 1, is_day ^ 1))
                        dist[nx][ny][k + 1] = t + 1
                    elif is_day == 0 and dist[nx][ny][k + 1] > t + 2:
                        q.append((nx, ny, k + 1, t + 2, is_day))
                        dist[nx][ny][k + 1] = t + 2

    
    ret_val = min(dist[-1][-1])
    return ret_val if ret_val != inf else -1




input = stdin.readline
row, col, crash = map(int, input().split())
arr = []
for _ in range(row):
    arr.append(list(input().rstrip()))
print(solve(arr, crash))
