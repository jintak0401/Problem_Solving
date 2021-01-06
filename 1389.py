from sys import stdin
input = stdin.readline

def solve():

    n, m = map(int, input().split())

    arr = [[0] * n for _ in range(n)]

    for _ in range(m):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        arr[a][b] = 1
        arr[b][a] = 1


    for i in range(n):
        for j in range(n):
            for k in range(n):
                if j == k:
                    continue
                if arr[j][i] > 0 and arr[i][k] > 0:
                    if arr[j][k] > arr[j][i] + arr[i][k]:
                        arr[j][k] = arr[j][i] + arr[i][k]
                    elif arr[j][k] == 0:
                        arr[j][k] = arr[j][i] + arr[i][k]

    min_val = 100000
    ans = 0
    for i in range(n):
        tmp_val = sum(arr[i])
        if min_val > tmp_val:
            min_val = tmp_val
            ans = i

    print(ans + 1)
    return

solve()
