from sys import stdin
input = stdin.readline

def solve():

    row, col = map(int, input().split())
    arr = [[0] * (col + 2)]
    for _ in range(row):
        arr.append([0] + list(map(int, list(input().rstrip()))) + [0])
    arr.append([0] * (col + 2))

    for i in range(1, row + 1):
        for j in range(1, col + 1):
            if arr[i][j] != 0:
                arr[i][j] = min(arr[i-1][j], arr[i][j-1], arr[i-1][j-1]) + 1

    ans = 0
    for i in range(1, row + 1):
        ans = max(max(arr[i]), ans)
    print(ans ** 2)

solve()
