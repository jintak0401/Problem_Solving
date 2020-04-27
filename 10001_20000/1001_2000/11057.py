from sys import stdin

input = stdin.readline

def solve():
    MOD = 10007
    N = int(input())
    dp = [[0] * 10 for _ in range(N + 1)]
    
    for i in range(10):
        dp[1][i] = 1

    for i in range(2, N + 1):
        for j in range(10):
            dp[i][j] = sum(dp[i-1][:j+1]) % MOD

    ans = sum(dp[N]) % MOD
    print(ans)
    return

solve()
