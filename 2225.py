from sys import stdin
input = stdin.readline

def solve():

    n, k = map(int, input().split())

    if k == 1:
        print(1)
        return

    elif k == 2:
        print(n + 1)
        return

    dp = [0 for i in range(n + 1)]
    dp[0] = 1
    MOD = 1000000000

    for i in range(k):
        for j in range(1, n + 1):
            dp[j] = (dp[j] + dp[j-1]) % MOD
    
    print(dp[n])
    return

solve()
