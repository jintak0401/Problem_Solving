from sys import stdin
from collections import deque, defaultdict
from heapq import *
input = stdin.readline

inf = float('inf')
def solve(dic, target, villege_num):
    
    dist = [inf for _ in range(villege_num)]
    dist[target] = 0 
    h = []
    heappush(h, (0, target))

    while h:
        d1, dst1 = heappop(h)
        for dst2, d2 in dic[dst1].items():
            if dist[dst2] > d1 + d2:
                dist[dst2] = d1 + d2
                heappush(h, (dist[dst2], dst2))

    return dist

        

n, m, x = map(int, input().split())
x -= 1
dic1 = defaultdict(dict)
dic2 = defaultdict(dict)
for _ in range(m):
    _from, _to, time = map(int, input().split())
    _from -= 1
    _to -= 1
    dic1[_from][_to] = time
    dic2[_to][_from] = time

print(max([a + b for a, b in zip(solve(dic1, x, n), solve(dic2, x, n))]))
