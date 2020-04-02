from sys import stdin
from collections import deque

min_val = 0
max_val = 0

def can_bfs(arr, diff):
    for i in range(min_val, max_val - diff + 1):
        if bfs(arr, i, i + diff):
            return True
    return False

def bfs(arr, down, up):

    if not (down <= arr[0][0] <= up and down <= arr[-1][-1] <= up):
        return False

    d = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    q = deque([(0, 0)])
    visited = set([(0, 0)])
    target = (len(arr) - 1, len(arr[0]) - 1)

    while q:
        pt = q.pop()
        if pt == target:
            return True
        for dx, dy in d:
            x, y = pt[0] + dx, pt[1] + dy
            if 0 <= x < len(arr) and 0 <= y < len(arr[0]):
                if down <= arr[x][y] <= up and (x, y) not in visited:
                    q.append((x, y))
                    visited.add((x, y))

    return False


def solve(arr, min_val, max_val):

    left = 0
    right = max_val - min_val

    while right >= left:
        mid = (right + left) // 2
        if can_bfs(arr, mid):
            right = mid - 1
        else:
            left = mid + 1
             
    return right + 1

input = stdin.readline

size = int(input())
arr = []
num = set()
for _ in range(size):
    user_input = list(map(int, input().split()))
    arr.append(user_input)
    min_val = min(min_val, min(user_input))
    max_val = max(max_val, max(user_input))

print(solve(arr, min_val, max_val))
