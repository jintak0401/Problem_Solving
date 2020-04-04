from sys import stdin
from collections import defaultdict
from heapq import *
input = stdin.readline

inf = float('inf')
dist = defaultdict(dict)
vertex = 0
edge = 0
start_pt = 0

def solve():

    h = []
    heappush(h, (0, start_pt))
    ret_val = [inf for _ in range(vertex + 1)]
    ret_val[start_pt] = 0

    while h:
        d1, dest1 = heappop(h)
        for dest2, d2 in dist[dest1].items():
            if ret_val[dest2] > d1 + d2:
                ret_val[dest2] = d1 + d2
                heappush(h, (ret_val[dest2], dest2))

    return ret_val[1:]

vertex, edge = map(int, input().split())
start_pt = int(input())

for _ in range(edge):
    u, v, w = map(int, input().split())
    if v in dist[u]:
        dist[u][v] = min(dist[u][v], w)
    else:
        dist[u][v] = w

ans = solve()
for i in ans:
    print(i if i != inf else 'INF')
