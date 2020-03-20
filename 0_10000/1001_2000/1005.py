from sys import stdin
from collections import deque

input = stdin.readline

case_num = int(input())

result = []

for _ in range(case_num):

    building, line = map(int, input().split())
    cost = list(map(int, input().split()))

    node_graph = [[] for _ in range(building)]
    line_graph = [0 for _ in range(building)]

    for _ in range(line):

        start, end = map(int, input().split())

        start -= 1
        end -= 1

        node_graph[start].append(end)
        line_graph[end] += 1

    target = int(input()) - 1

    q = deque([])

    ans = [0 for _ in range(building)]

    for i in range(building):
        if line_graph[i] == 0:
            q.append(i)
            ans[i] = cost[i]

    while True:

        node = q.popleft()

        for i in node_graph[node]:
            line_graph[i] -= 1
            ans[i] = max(ans[node] + cost[i], ans[i])
            if line_graph[i] == 0:
                q.append(i)

        if line_graph[target] == 0:
            break

    result.append(str(ans[target]))

print('\n'.join(result))

