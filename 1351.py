from sys import stdin, setrecursionlimit as SRL
SRL(10 ** 6)

input = stdin.readline

def solve():

    n, p, q = map(int, input().split())
    if n == 0:
        print(1)
        return
    dp = {0 : 1}

    def get_val(idx):
        if idx in dp:
            return dp[idx]

        dp[idx] = get_val(idx // p) + get_val(idx // q)
        return dp[idx]

    print(get_val(n // p) + get_val(n // q))
    return

solve()
