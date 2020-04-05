from sys import stdin
from heapq import *
from collections import defaultdict
input = stdin.readline

ans = 0
confirmed = set()
edge = defaultdict(list)

def solve(edge):

    global ans, confirmed
    h = []
    confirmed.add(1)
    for tmp in edge[1]:
        heappush(h, tmp)

    while len(confirmed) != v:
        _edge = heappop(h) 
        if _edge[1] not in confirmed or _edge[2] not in confirmed:
            ans += _edge[0]
            confirmed |= {_edge[1], _edge[2]}
            for tmp in edge[_edge[2]]:
                heappush(h, tmp)

v, e = map(int, input().split())

for _ in range(e):
    a, b, c = map(int, input().split())
    edge[a].append((c, a, b))
    edge[b].append((c, b, a))
    
solve(edge)
print(ans)
