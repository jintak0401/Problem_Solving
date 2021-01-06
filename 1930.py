from sys import stdin
from collections import Counter
input = stdin.readline

def compare(a, b):

    if Counter(a) != Counter(b):
        return False

    for i in range(4):
        comp = [*b]
        comp[0], comp[i] = comp[i], comp[0]
        if i != 0:
            tmp = (2, 3) if i == 1 else (1, 3) if i == 2 else (1, 2)
            comp[tmp[0]], comp[tmp[1]] = comp[tmp[1]], comp[tmp[0]]
        for _ in range(4):
            comp[1:] = comp[2:] + comp[1:2]
            if comp == a:
                return True
    return False

def solve():

    test_case = int(input())

    for _ in range(test_case):
        tmp = list(map(int, input().split()))
        a = tmp[:4]
        b = tmp[4:]

        if compare(a, b):
            print(1)
        else:
            print(0)

solve()
