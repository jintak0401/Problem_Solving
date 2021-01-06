from sys import stdin
from bisect import bisect_left

input = stdin.readline

def solve():
    
    n = int(input())
    arr = list(map(int, input().split()))
    
    dp = [arr[0]]
    ans = [0 for i in range(n)]
    ans[0] += 1
    ans[-1] += 1

    for i in range(1, n):
        if dp[-1] < arr[i]:
            dp.append(arr[i])
        else:
            dp[bisect_left(dp, arr[i])] = arr[i]
        ans[i] += len(dp)

    dp = [arr[-1]]
    for i in range(n - 2, 0, -1):
        if dp[-1] < arr[i]:
            dp.append(arr[i])
        else:
            dp[bisect_left(dp, arr[i])] = arr[i]
        ans[i] += len(dp)
    
    print(max(ans) - 1)
    return

solve()
