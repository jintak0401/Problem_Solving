from sys import stdin

input = stdin.readline

def solve():
    input()
    arr = list(map(int, input().split()))
    arr = sorted(arr)
    num = int(input())
    _range = [0, arr[-1]]
    for i in range(len(arr)):
        if arr[i] == num:
            return 0
        elif arr[i] < num:
            _range[0] = arr[i]
        else:
            _range[1] = arr[i]
            break

    ret = (_range[1] - num) * (num - _range[0] - 1) + (_range[1] - num - 1)
    return ret


print(solve())
