from sys import stdin
from collections import defaultdict
input = stdin.readline

inf = 10 ** 10

def solve(graph, vertex):

    arr = [inf for _ in range(vertex)]
    arr[0] = 0
    for _ in range(vertex):
        check = True
        for src, dist in graph.items():
            for dest, d in dist.items():
                if arr[dest] > arr[src] + d:
                    arr[dest] = arr[src] + d
                    check = False
        if check:
            break

    return 'NO' if check else 'YES'

case_num = int(input())

for _ in range(case_num):
    vertex, road, wormhole = map(int, input().split())
    graph = defaultdict(dict)
    for _ in range(road):
        s, e, t = map(int, input().split())
        s, e = s - 1, e - 1

        if e in graph[s]:
            graph[s][e] = min(graph[s][e], t)
            graph[e][s] = graph[s][e]
        else:
            graph[s][e] = t
            graph[e][s] = t

    for _ in range(wormhole):
        s, e, t = map(int, input().split())
        s, e = s - 1, e - 1
        if e in graph[s]:
            graph[s][e] = min(graph[s][e], -t)
        else:
            graph[s][e] = -t

    print(solve(graph, vertex))
