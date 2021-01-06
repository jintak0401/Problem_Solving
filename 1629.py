
a, b, c = map(int, input().split())
a %= c

dp = {}

dp[0] = 1
dp[1] = a

idx = 1
pos = 0

while pos != b:

    if idx == 0:
        exit(0)
    if pos + idx <= b:
        dp[pos + idx] = (dp[pos] * dp[idx]) % c
        pos = pos + idx
        idx = 2 * idx if pos > 1 else 1

    else:
        idx //= 2

print(dp[b])
