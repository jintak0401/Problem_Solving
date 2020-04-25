from sys import stdin
from bisect import bisect_left
input = stdin.readline

def solve(arr):

    inf = float('inf')
    LIS_check = [inf for _ in range(len(arr))]
    pos = [-1 for _ in range(len(arr))]
    length = -1
    for i in range(len(arr)):
        tmp = bisect_left(LIS_check, arr[i])
        pos[i] = tmp
        LIS_check[tmp] = arr[i]
        length = max(length, tmp + 1)

    composed_LIS = set()
    idx = length - 1
    for i in range(len(arr) - 1, -1, -1):
        if pos[i] == idx:
            composed_LIS.add(arr[i])
            idx -= 1
            if idx == -1:
                break

    ans = set(arr) - composed_LIS

    return len(arr) - length, sorted(list(ans))

size = int(input())
mapping = []
for _ in range(size):
    mapping.append(tuple(map(int, input().split())))

mapping.sort(key = lambda x : (x[1]))
length, ans = solve([mapping[i][0] for i in range(len(mapping))])
print(length)
print(*ans, sep='\n')
