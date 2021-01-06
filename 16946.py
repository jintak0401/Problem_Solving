from sys import stdin
from collections import deque
input = stdin.readline

d = [(1, 0), (-1, 0), (0, 1), (0, -1)]
area = {}
S = {}
def divide_area(arr):
    
    zone = 0
    for i in range(n):
        for j in range(m):
            if arr[i][j] == '0':
                zone += 1
                q = deque([(i, j)])
                S[zone] = 1
                arr[i][j] = zone
                while q:
                    pt = q.popleft()
                    for dx, dy in d:
                        x, y = pt[0] + dx, pt[1] + dy
                        if 0 <= x < n and 0 <= y < m:
                            if arr[x][y] == '0':
                                S[zone] += 1
                                q.append((x, y))
                                arr[x][y] = zone
                


def solve(arr, pt):
    zone = set()
    for dx, dy in d:
        x, y = pt[0] + dx, pt[1] + dy
        if 0 <= x < n and 0 <= y < m and arr[x][y] != '1':
            zone |= {arr[x][y]}

    ret_val = 1
    for i in zone:
        ret_val += S[i]
    return str(ret_val % 10)


n, m = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(list(input().rstrip()))

divide_area(arr)
for i in range(n):
    tmp = ['0'] * m
    for j in range(m):
        if arr[i][j] == '1':
            tmp[j] = solve(arr, (i, j))
    print(''.join(tmp))
