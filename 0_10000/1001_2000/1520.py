from sys import stdin, setrecursionlimit as SRL
SRL(10 ** 6)

input = stdin.readline

def solve():
    M, N = map(int, input().split())
    dp = [[-1] * N for _ in range(M)]
    d = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    arr = []
    for _ in range(M):
        arr.append(list(map(int, input().split())))

    def dfs(nx, ny):

        if dp[nx][ny] != -1:
            return dp[nx][ny]

        elif nx == M - 1 and ny == N - 1:
            return 1

        ret_val = 0
        for dx, dy in d:
            x, y = nx + dx, ny + dy
            if 0 <= x < M and 0 <= y < N and arr[nx][ny] > arr[x][y]:
                ret_val += dfs(x, y)
        dp[nx][ny] = ret_val
        return ret_val

    print(dfs(0, 0))
    return

solve()
