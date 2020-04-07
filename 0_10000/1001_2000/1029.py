from sys import stdin
input = stdin.readline

def solve(price, person, history):

    global trade, dp
    if dp[person][price][history] != 0:
        return dp[person][price][history]
    ret_val = 1
    add = 0
    for i in range(len(trade)):
        if trade[person][i] >= price and history & (1 << i) == 0:
            add = max(add, solve(trade[person][i], i, history | (1 << i)))
    dp[person][price][history] = ret_val + add
    return dp[person][price][history]

size = int(input())

trade = [list(map(int, list(input().rstrip()))) for _ in range(size)]
dp = [[[0 for _ in range(1 << size)] for _ in range(10)] for _ in range(size)]
print(solve(0, 0, 1))
