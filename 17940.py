from sys import stdin
from collections import defaultdict
from heapq import *
input = stdin.readline

change = 10 ** 6
def solve(dist, target):
    
    inf = float('inf')
    h = []
    heappush(h, (0, 0)) # dist, node
    ret_val = [inf for _ in range(len(dist))]
    ret_val[0] = 0
    while h:
        d, node = heappop(h) 
        if node == target:
            return d // change, d % change
        for dst, d2 in dist[node].items():
            if ret_val[dst] > d + d2:
                heappush(h, (d + d2, dst))
                ret_val[dst] = d + d2

n, target = map(int, input().split())
line = [int(input()) for _ in range(n)]

dist = defaultdict(dict)
for i in range(n):
    tmp = [*map(int, input().split())]
    for j in range(len(tmp)):
        if tmp[j] != 0:
            if line[i] == line[j]:
                dist[i][j] = tmp[j]
            else:
                dist[i][j] = tmp[j] + change

print(*solve(dist, target))
