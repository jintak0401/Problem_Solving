from sys import stdin
from bisect import bisect_left

input = stdin.readline

def solve():
    
    n = int(input())
    arr = list(map(int, input().split()))
    
    asc = [arr[0]]
    asc_len = [0 for _ in range(n)]
    desc = [arr[-1]]
    desc_len = [0 for _ in range(n)]
    asc_len[0], desc_len[-1] = 1, 1

    for i in range(1, n):
        if asc[-1] < arr[i]:
            asc.append(arr[i])
        else:
            asc[bisect_left(asc, arr[i])] = arr[i]
        if desc[-1] < arr[-i - 1]:
            desc.append(arr[-i - 1])
        else:
            desc[bisect_left(desc, arr[-i - 1])] = arr[-i - 1]

        asc_len[i] = len(asc)
        desc_len[-i - 1] = len(desc)
    
    ans = 0
    for i in range(n):
        ans = max(ans, asc_len[i] + desc_len[i] - 1)
    print(ans)
    return

solve()
