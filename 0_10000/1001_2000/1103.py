from sys import stdin, setrecursionlimit as SRL
input = stdin.readline
SRL(10 ** 5)

d = [(1, 0), (-1, 0), (0, 1), (0, -1)]
def dfs(nx, ny, visited):
    global d, arr, row, col, dp
    if arr[nx][ny] == 'H':
        return 0
    elif dp[nx][ny] != 0:
        return dp[nx][ny]
    ret_val = 1
    num = int(arr[nx][ny])
    for dx, dy in d:
        x, y = nx + dx * num, ny + dy * num
        if 0 <= x < row and 0 <= y < col:
            if (x, y) in visited:
                return -1
            else:
                val = dfs(x, y, visited | {(x, y)})
                if val == -1:
                    return -1
                else:
                    ret_val = max(1 + val, ret_val)
    dp[nx][ny] = ret_val
    return ret_val

row, col = map(int, input().split())
dp = [[0] * col for _ in range(row)]
arr = []
for _ in range(row):
    tmp = list(input().rstrip())
    arr.append([*tmp])

print(dfs(0, 0, {(0, 0)}))
