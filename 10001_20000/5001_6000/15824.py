from sys import stdin

input = stdin.readline
MOD = 1000000007

length = int(input())

arr = sorted(list(map(int, input().split())))

ans = 0

power = [1]
for _ in range(length):
    val = (power[-1] << 1) % MOD
    power.append(val)

for i in range(length):
    ans += arr[i] * (power[i] - power[length - i - 1])
    ans %= MOD

print(ans % MOD)
