from sys import stdin



mod = 1000000007
input = stdin.readline

def get_gcd(a, b):
    if b == 0:
        return a, 1, 0
    else:
        gcd, x, y = get_gcd(b, a % b)
        return gcd, y, x - (a // b) * y


n, k = map(int, input().split())

bracket = [0 for _ in range(2 * n + 1)]
color = [0 for _ in range(n)]
S = [0 for _ in range(n + 1)]

bracket[0] = 1
color[0] = 1
S[0] = 1

for i in range(1, 2 * n + 1):
    bracket[i] = bracket[i - 1] * i % mod

for i in range(1, n // 2 + 1):
    color[i] = color[i - 1] * k % mod

for i in range(1, n + 1):

    S[i] = S[i - 1] * (k + 1) % mod

    if i % 2 == 1:

        num = (bracket[(i // 2) * 2] * (get_gcd(bracket[i // 2] * bracket[i // 2 + 1] % mod, mod))[1] % mod + mod) % mod
        S[i] = (S[i] - (color[i // 2] * num) % mod + mod) % mod

print(S[n])
