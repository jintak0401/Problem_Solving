import bisect
from sys import stdin

input = stdin.readline

length = int(input())

arr = list(map(int, input().split()))

lis_len = [arr[0]]
lis_str = [0 for _ in range(len(arr))]

for i in range(1, len(arr)):

    if arr[i] > lis_len[-1]:
        lis_str[i] = len(lis_len)
        lis_len.append(arr[i])

    else:
        pos = bisect.bisect_left(lis_len, arr[i])
        lis_str[i] = pos
        lis_len[pos] = arr[i]


print(len(lis_len))


# ans = [0 for _ in range(len(lis_len))]

# for i in range(len(lis_str)):
    # ans[lis_str[i]] = arr[i]

# print(ans)
