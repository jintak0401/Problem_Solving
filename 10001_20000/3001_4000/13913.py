from collections import deque

def solve(n, k):

    q = deque([(n, 0b11)])
    visited = set()

    while True:
       
        pt, path = q.popleft()
        if pt == k:
            return pt, path
        elif pt < 0:
            continue
        
        if pt + 1 not in visited:
            q.append((pt + 1, path << 2 | 0b10))
            visited.add(pt + 1)
        if pt - 1 not in visited:
            q.append((pt - 1, path << 2 | 0b01))
            visited.add(pt - 1)
        if pt != 0 and pt < k and pt * 2 not in visited:
            q.append((pt * 2, path << 2 | 0b00))
            visited.add(pt * 2)

n, k = map(int, input().split())
_, path = solve(n, k)

ans = deque([k])

while path != 0b11:
    val = path & 0b11

    if val == 0b01:
        k += 1

    elif val == 0b10:
        k -= 1

    else:
        k //= 2

    ans.appendleft(k)
    path >>= 2


print(len(ans) - 1)
print(' '.join(map(str, ans)))
