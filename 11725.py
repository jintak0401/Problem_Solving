from sys import stdin
from collections import deque

def solve(arr):

    ans = [-1] * len(arr)
    q = deque([1])
    
    while q:
        num = q.popleft()
        for i in arr[num]:
            if ans[i] == -1:
                ans[i] = num
                q.append(i)

    return ans

input = stdin.readline
size = int(input())

arr = [[] for _ in range(size + 1)]
for _ in range(size - 1):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)

ans = solve(arr)
print('\n'.join(map(str, ans[2:])))
