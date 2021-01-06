from sys import stdin
from bisect import bisect_left
input = stdin.readline

def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    inf = float('inf') 
    brr = [inf for _ in range(n)]
    idx = [0 for _ in range(n)] 

    for i in range(n):
        idx[i] = bisect_left(brr, arr[i])
        brr[idx[i]] = arr[i]

    print(max(idx) + 1)
    return

solve()
