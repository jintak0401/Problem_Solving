def solve(num):
    MOD = 10007
    dp = [0 for I in range(max(num + 1, 3))]
    dp[1] = 1
    dp[2] = 3
    for i in range(3, num + 1):
        dp[i] = (dp[i-2] * 2 + dp[i-1]) % MOD
    return dp[num]

num = int(input())
print(solve(num))
