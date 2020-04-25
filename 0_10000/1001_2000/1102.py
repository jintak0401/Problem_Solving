from sys import stdin
from heapq import *
input = stdin.readline

inf = float('inf')
cost = []

def get_min(num, dst):
    global cost

    src = 0
    ret_val = inf
    while num != 0:
        if num & 1:
            ret_val = min(ret_val, cost[src][dst])
        src += 1
        num >>= 1
    return ret_val

def solve():

    global cost
    N = int(input())
    for _ in range(N):
        cost.append(list(map(int, input().split())))

    can_use = input()
    bitmask = 0
    cnt = 0
    for i in range(N):
        if can_use[i] == 'Y':
            bitmask |= 1 << i
            cnt += 1

    P = int(input())
    P -= cnt
    dp = [[None] * ((1 << N) - 1) for _ in range(max(1, P + 1))]

    def fixing(bit, remain):

        global inf, cost

        if remain == 0:
            return 0

        elif dp[remain][bit] is not None:
            return dp[remain][bit]

        else:
            ret_val = inf
            for dst in range(len(cost)):
                if bit & (1 << dst) == 0:
                    ret_val = min(ret_val, fixing(bit | (1 << dst), remain - 1) + get_min(bit, dst))
            dp[remain][bit] = ret_val

            return ret_val

    ans = fixing(bitmask, max(P, 0))
    print(ans if ans != inf else -1)

solve()
