from sys import stdin, setrecursionlimit as SRL
from collections import defaultdict
SRL(10 ** 5)

dist = defaultdict(dict)

def dfs(node, visited):
    dest, d = node, 0
    for x in dist[node]:
        if x not in visited:
            visited.add(x)
            tmp_dest, tmp_d = dfs(x, visited | {x})
            tmp_d += dist[node][x]
            if d < tmp_d:
                dest, d = tmp_dest, tmp_d

    return dest, d



input = stdin.readline
num = int(input())
for i in range(num):
    tmp = list(map(int, input().split()))[:-1]
    for j in range(1, len(tmp), 2):
        dist[tmp[0]][tmp[j]] = tmp[j + 1]
    
dest, _ = dfs(1, {1})
_, d = dfs(dest, {dest})
print(d)
