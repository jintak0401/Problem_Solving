from sys import stdin
from collections import deque, defaultdict
input = stdin.readline

def solve(n, k):
    if n >= k:
        return n - k, 1
    
    q = deque([n])
    time = 0
    ret_time = -1
    ret_num = 0
    visited = {n}
    while q:
        q_len = len(q)
        for _ in range(q_len):
            pos = q.popleft()
            visited.add(pos)
            if pos == k:
                ret_time = time
                ret_num += 1
            elif ret_time == -1: 
                if ((2 * pos <= k) or (2 * pos - k < k - pos)) and (2 * pos not in visited):
                    q.append(2 * pos)

                if pos + 1 <= k and pos + 1 not in visited:
                    q.append(pos + 1)

                if pos - 1 > 0 and pos - 1 not in visited:
                    q.append(pos - 1)

        if ret_time != -1:
            return ret_time, ret_num
        else:
            time += 1

n, k = map(int, input().split())
print(*solve(n, k), sep = '\n')
