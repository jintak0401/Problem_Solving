N, r, c = map(int, input().split())

ans = 0

while N != 0:
   
    tmp = 2 ** (N - 1)
    pos = 2 * (r // tmp) + (c // tmp)
    ans += pos * (tmp ** 2)
    N -= 1
    r %= tmp
    c %= tmp

print(ans)

