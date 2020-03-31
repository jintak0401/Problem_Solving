from sys import stdin
from collections import defaultdict

def dfs(item, path, n, dist, visited):
   
    if n in visited:
        ret_val = 0
    else:
        ret_val = item[n]
        visited.add(n)

    for i in path[n]:
        if dist >= path[n][i]:
            ret_val += dfs(item, path, i, dist - path[n][i], visited)
            
    return ret_val

input = stdin.readline
zone, dist, path_num = map(int, input().split())
item = list(map(int, input().split()))
path = defaultdict(dict)
for _ in range(path_num):
    a, b, c = map(int, input().split())
    path[a - 1][b - 1] = c
    path[b - 1][a - 1] = c

ans = 0
for i in range(zone):
    visited = set()
    ans = max(ans, dfs(item, path, i, dist, visited))
print(ans)
