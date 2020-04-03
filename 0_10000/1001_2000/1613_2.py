from sys import stdin
from collections import defaultdict
from copy import deepcopy
input = stdin.readline

n, k = map(int, input().split())
before = defaultdict(set)
after = defaultdict(set)
for _ in range(k):
    a, b = map(int, input().split())
    before[a] |= {b}
    after[b] |= {a}

for i in range(1, n + 1):
    tmp_before = deepcopy(before[i])
    tmp_after = deepcopy(after[i])
    for j in tmp_before:
        before[i] |= before[j]
        after[j] |= after[i]
    for j in tmp_after:
        after[i] |= after[j]
        before[j] |= before[i]

q_num = int(input())

for _ in range(q_num):
    a, b = map(int, input().split())
    if b in after[a]:
        print(1)
    elif b in before[a]:
        print(-1)
    else:
        print(0)
