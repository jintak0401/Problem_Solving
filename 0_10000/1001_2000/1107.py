from itertools import product
from sys import stdin
from bisect import bisect_left


target = int(input())
ans1 = abs(target - 100)

broken_len = int(input())

arr = [i for i in range(10)]
if broken_len > 0:
    broken = set([i for i in map(int, input().split())])
    arr = set(arr)
    arr -= broken
    arr = sorted(list(arr))

if broken_len == 10 or target == 100:
    print(ans1)


else:

    pro = list(map(int, map(''.join, (product(map(str, arr), repeat=len(str(target)))))))
    idx = bisect_left(pro, target)
    idx = idx if (idx == 0) or (idx != len(pro) and pro[idx] - target < target - pro[idx - 1]) else idx - 1
    diff = abs(target - pro[idx])
    num = pro[idx]

    if len(str(target)) > 1:
        pro = list(map(int, map(''.join, (product(map(str, arr), repeat=len(str(target)) - 1)))))
        idx = bisect_left(pro, target)
        idx = idx if (idx == 0) or (idx != len(pro) and pro[idx] - target < target - pro[idx - 1]) else idx - 1
        if diff >= abs(target - pro[idx]):
            num = pro[idx]
            diff = abs(target - num)

    pro = list(map(int, map(''.join, (product(map(str, arr), repeat=len(str(target)) + 1)))))
    idx = bisect_left(pro, target)
    idx = idx if (idx == 0) or (idx != len(pro) and pro[idx] - target < target - pro[idx - 1]) else idx - 1
    if diff > abs(target - pro[idx]):
        num = pro[idx]
        diff = abs(target - num)

    print(min(ans1, diff + min(abs(num - 100), len(str(num))))) 




