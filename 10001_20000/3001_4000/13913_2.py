from collections import deque

LIMIT = 0
prev = {}
def solve(n, k): 
    global prev, LIMIT

    if n >= k:
        return n - k, list(range(n, k - 1, -1))

    elif n < k <= 2 * n:
       
        up, down = k - n, 1 + (n - (k + k % 2) // 2) + k % 2
        if up < down:
            return up, list(range(n, k + 1))
        else:
            return down, [*range(n, (k + k % 2) // 2 - 1, -1), *range(k + k % 2, k - 1, -1)]

    q = deque([n])
    visited = {n}
    step = 0
    while True:
       
        q_size = len(q)

        for _ in range(q_size):
            pt = q.popleft()

            pos = [i for i in [pt - 1, pt + 1, 2 * pt] if 0 <= i <= LIMIT]

            for x in pos:

                if x not in visited:
                    prev[x] = pt
                    if x == k: return step + 1, get_path(n, k)

                    q.append(x)
                    visited.add(x)

        step += 1

def get_path(n, k):
    
    global prev
    ret_val = [k]
    pos = k 
    while pos != n:
        ret_val.append(prev[pos])
        pos = prev[pos]
    
    return ret_val[::-1]


n, k = map(int, input().split())
LIMIT = k + k % 2
length, path = solve(n, k)
print(length)
print(*path)
