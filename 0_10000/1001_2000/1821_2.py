from sys import stdin
from itertools import permutations
input = stdin.readline

def solve():

    N, F = map(int, input().split())
    arr = [i for i in range(1, N + 1)]
    comb = [0 for i in range(N)]
    comb[0] = 1
    comb[-1] = 1

    for i in range(1, (N // 2) + (N % 2)):
        comb[i] = comb[i-1] * (N - i) // i
        comb[-i-1] = comb[i]

    for perm in permutations(range(1, N + 1), N):
        if sum(a * b for a, b in zip(comb, perm)) == F:
            print(*perm)
            return

solve()
