from sys import stdin
from collections import deque

input = stdin.readline
d = [[1, 0], [-1, 0], [0, 1], [0, -1]]

size = int(input())

ans = []
arr = []

for _ in range(size):
    arr.append(list(input().rstrip()))

for i in range(size):
    for j in range(size):
        
        if arr[i][j] == '1':
            s = [(i, j)]
            arr[i][j] = '0'
            ans.append(1)
            while s:
                pt = s.pop()
                for dx, dy in d:
                    tmp_pt = (pt[0] + dx, pt[1] + dy)
                    if 0 <= tmp_pt[0] < size and 0 <= tmp_pt[1] < size and arr[tmp_pt[0]][tmp_pt[1]] =='1':
                        arr[tmp_pt[0]][tmp_pt[1]] = '0'
                        ans[-1] += 1
                        s.append(tmp_pt)

ans.sort()

print(len(ans))
print('\n'.join(map(str, ans)))



