from sys import stdin
from collections import defaultdict, Counter
input = stdin.readline

size = int(input())
arr = [[] for _ in range(4)]
for _ in range(size):
    tmp = list(map(int, input().split()))
    for i in range(4):
        arr[i].append(tmp[i])

for i in range(4):
    arr[i] = Counter(arr[i])

dic = defaultdict(int)
for i in arr[0]:
    for j in arr[1]:
        dic[i + j] += arr[0][i] * arr[1][j]

ans = 0
for i in arr[2]:
    for j in arr[3]:
        if -(i + j) in dic:
            ans += dic[-(i + j)] * arr[2][i] * arr[3][j]

print(ans)
