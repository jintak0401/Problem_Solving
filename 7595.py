from sys import stdin
from collections import deque

input = stdin.readline

def solve():

    N, M = map(int, input().split())

    m = list(map(int, input().split()))
    c = list(map(int, input().split()))

    dp = [[0] * (100 * N) for _ in range(N)] # dp[N][100 * N]
    dp[0][c[0]] = m[0]

    ans = float('inf')
    for i in range(1, N):
        for j in range(100 * N):
            if j - c[i] >= 0:
                dp[i][j] = max(dp[i][j], dp[i-1][j-c[i]] + m[i])

            dp[i][j] = max(dp[i-1][j], dp[i][j])
            
            if dp[i][j] >= M:
                ans = min(ans, j)

    print(ans)

solve()
