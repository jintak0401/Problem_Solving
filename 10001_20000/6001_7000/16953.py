from sys import stdin
from collections import deque
input = stdin.readline

def solve(_from, _to):
    
    ret_val = 1

    q = deque([_from])

    while q:
        
        q_len = len(q)
        for _ in range(q_len):
            num = q.popleft()
            if num == _to:
                return ret_val
            else:
                if 2 * num <= _to:
                    q.append(2 * num)
                if num * 10 + 1 <= _to:
                    q.append(10 * num + 1)
        ret_val += 1
    return -1

_from, _to = map(int, input().split())
print(solve(_from, _to))
