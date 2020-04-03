from sys import stdin
input = stdin.readline

n, k = map(int, input().split())
arr = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
for _ in range(k):
    a, b = map(int, input().split())
    arr[a][b] = -1
    arr[b][a] = 1

for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i == j or arr[i][j] != 0:
                continue
            elif arr[i][k] == arr[k][j] and arr[i][k] != 0:
                arr[i][j] = arr[i][k]
                arr[j][i] = -arr[i][k]

q_num = int(input())

for _ in range(q_num):
    a, b = map(int, input().split())
    print(arr[a][b])
