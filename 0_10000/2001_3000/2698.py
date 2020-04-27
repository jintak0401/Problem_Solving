from sys import stdin
from collections import deque
input = stdin.readline

def solve():
    test_case = int(input())
    for _ in range(test_case):

        n, k = map(int, input().split())

        zero = deque([0 for _ in range(k + 1)])
        one = deque([1])
        zero[0] = 1

        for i in range(1, n):
            one.appendleft(0)
            for j in range(min(i, k + 1)):
                val = zero[j]
                zero[j] += one[j+1]
                one[j] += val

        print(zero[k] + one[k])

solve()
