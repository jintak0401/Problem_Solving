from sys import stdin
from collections import Counter
input = stdin.readline

def get_len(arr, h):
    return sum([(k - h) * v if k > h else 0 for k, v in arr.items()])

def solve(arr, target):
    up = max(arr.keys())
    down = up - target if up >= target else 0
    ret_val = 0
    while down <= up:
        mid = (down + up) // 2
        _len = get_len(arr, mid)
        if _len >= target:
            ret_val = mid
            down = mid + 1
        else:
            up = mid - 1
    return ret_val

_, target = map(int, input().split())
arr = Counter(map(int, input().split()))
print(solve(arr, target))
