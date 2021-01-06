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

    # (n + 1) H (k - 1) == (n + k - 1) C (k - 1)

    N = n + k - 1
    R = k - 1 if k - 1 < N // 2 else n
    MOD = 1000000000

    up = 1
    down = 1
    for i in range(R):
        up *= (N - i)
        down *= (R - i)

    print((up // down) % MOD)

    return

solve()
