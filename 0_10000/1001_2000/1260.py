from collections import deque
import sys

def bfs(arr, index):

    q = deque([])
    visited = set([])

    while True:

        if index in visited:
            if len(q) == 0:
                break

            index = q.popleft()
            continue

        print(index, end = ' ')

        visited.add(index)

        if index in arr:
            for i in sorted(list(arr[index])):
                q.append(i)
            index = q.popleft()


def dfs(arr, index):

    s = deque([])
    visited = set([])

    while True:

        if index in visited:
            if len(s) == 0:
                break

            index = s.pop()
            continue

        print(index, end = ' ')

        visited.add(index)
        
        if index in arr :
            for i in sorted(list(arr[index]), reverse=True):
                s.append(i)
            index = s.pop()



input = sys.stdin.readline

n, m, v = map(int, input().split())

arr = {}

for i in range(m):
    a, b = map(int, input().split())

    if not a in arr:
        arr[a] = set([])

    if not b in arr:
        arr[b] = set([])

    arr[a].add(b)
    arr[b].add(a)


dfs(arr, v)
print()
bfs(arr, v)
print()



