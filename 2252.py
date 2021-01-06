from sys import stdin
from collections import defaultdict, deque
input = stdin.readline

def solve():
    global dic, directed, c
    ret_val = []
    q = deque([])
    for i in range(1, len(directed)):
        if directed[i] == 0:
            q.append(i)

    while q:
        person = q.popleft()
        ret_val.append(person)
        if person in dic:
            for i in dic[person]:
                directed[i] -= 1
                if directed[i] == 0:
                    q.append(i)
    return ret_val

n, m = map(int, input().split())
directed = [0] * (n + 1)
dic = defaultdict(set)
for _ in range(m):
    a, b = map(int, input().split())
    directed[b] += 1
    dic[a].add(b)
print(*solve())
