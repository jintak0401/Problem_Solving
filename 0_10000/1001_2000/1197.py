from sys import stdin
from heapq import *
input = stdin.readline

ans = 0
disjoint_set = []

def find(a):
    while disjoint_set[a] > 0:
        a = disjoint_set[a]
    return a

def union(a, b):
    _a = find(a)
    _b = find(b)
    if disjoint_set[_a] < disjoint_set[_b]:
        disjoint_set[_b] = _a
    else:
        if disjoint_set[_b] == disjoint_set[_a]:
            disjoint_set[_b] -= 1
        disjoint_set[_a] = _b
    

def solve(edge):

    global ans
    
    cnt = 0
    idx = 0
    while cnt != v - 1:
        dist, a, b = edge[idx]
        idx += 1
        if find(a) != find(b):
            union(a, b)
            ans += dist
            cnt += 1
    

v, e = map(int, input().split())
disjoint_set = [0 for _ in range(v + 1)]

edge = []
for _ in range(e):
    a, b, c = map(int, input().split())
    edge.append((c, a, b))

edge.sort(key = lambda x : (x[0]))
solve(edge)
print(ans)
