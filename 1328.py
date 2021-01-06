from sys import stdin
input = stdin.readline

def solve(building, left, right):
    MOD = 1000000007
    dp = [[[0 for _ in range(max(right + 1, 3))] for _ in range(max(left + 1, 3))] for _ in range(max(building + 1, 3))]
    dp[1][1][1] = 1
    dp[2][2][1] = dp[2][1][2] = 1

    for i in range(3, building + 1):
        for j in range(1, left + 1):
            for k in range(1, right + 1):
                dp[i][j][k] = (dp[i-1][j-1][k] + dp[i-1][j][k-1] + (i-2)*dp[i-1][j][k]) % MOD

    return dp[building][left][right]

building, left, right = map(int, input().split())
print(solve(building, left, right))
