dp = []
MOD = 1000000007

near = {0: (1, 2), 1 : (0, 2, 3), 2 : (0, 1, 3, 4), 3 : (1, 2, 4, 5), 4 : (2, 3, 5, 6), 5 : (3, 4, 7), 6 : (4, 7), 7 : (5, 6)}
def solve(d):
    for i in range(2, d + 1):
        for j in range(8):
            dp[j][i % 2] = 0
            for pos in near[j]:
                dp[j][i % 2] += dp[pos][(i - 1) % 2]
            dp[j][i % 2] %= MOD

    
d = int(input())
dp = [[0 for _ in range(2)] for _ in range(8)]

dp[1][1] = 1
dp[2][1] = 1
solve(d)
print(dp[0][d % 2])
