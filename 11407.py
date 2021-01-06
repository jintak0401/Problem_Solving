from sys import stdin

input = stdin.readline

def solve(coin, target):

    ans = 0
    idx = len(coin) - 1
    while target != 0:
        if coin[idx] > target:
            idx -= 1
            continue
        else:
            num = target // coin[idx]
            ans += num
            target -= num * coin[idx]
    return ans

coin_len, target = map(int, input().split())
coin = []

for _ in range(coin_len):
    coin.append(int(input()))

print(solve(coin, target))
