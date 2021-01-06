
mod = 10007

n = int(input())

combi = [[0 for _ in range(54 - j, 54)] for j in range(1, 54)]

combi[0][0] = 1
combi[1][0] = 1
combi[1][1] = 1

for i in range(2, 53):
    combi[i][0] = 1
    combi[i][i] = 1
    for j in range(1, len(combi[i]) - 1):
        combi[i][j] = combi[i - 1][j] + combi[i - 1][j - 1]
        combi[i][j] %= mod




dp = [[0 for _ in range(53)] for j in range(14)]
dp[0][0] = 1

for i in range(1, 14):
    for j in range(0, 4):
        for k in range(0, 53):
            if j + k <= n:
                dp[i][j + k] += dp[i - 1][k] * combi[4][j]
                dp[i][j + k] %= mod

print((combi[52][n] - dp[13][n] + mod) % mod)
