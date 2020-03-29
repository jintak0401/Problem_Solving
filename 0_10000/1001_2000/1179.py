import sys

sys.setrecursionlimit(2500)

def joseph(n, k):

    if k == 1 or n == 1:
        return n - 1

    elif k > n:
        ret_val = (joseph(n - 1, k) + k) % n
        return ret_val

    cnt = n // k
    res = joseph(n - cnt, k) - n % k
    if res < 0:
        res += n
    else:
        res += res // (k - 1)

    return res
    

n, k = map(int, input().split())
print(joseph(n, k) + 1)
