from sys import stdin
from collections import deque, defaultdict
input = stdin.readline

def solve(seq, directed_num):

    q = deque()
    for i in range(1, len(directed_num)):
        if directed_num[i] == 0:
            q.append(i)

    ret_val = []
    while q:
        singer = q.popleft()
        ret_val.append(singer)

        for nxt, val in seq[singer].items():
            directed_num[nxt] -= val
            if directed_num[nxt] == 0:
                q.append(nxt)

    return ret_val if len(ret_val) == len(seq) - 1 else [0]

singer_num, pd_num = map(int, input().split())
seq = [dict() for _ in range(singer_num + 1)]
directed_num = [0 for _ in range(singer_num + 1)]
for _ in range(pd_num):
    tmp = list(map(int, input().split()))[1:]
    for i in range(len(tmp) - 1):
        if tmp[i + 1] in seq[tmp[i]]:
            seq[tmp[i]][tmp[i + 1]] += 1
        else:
            seq[tmp[i]][tmp[i + 1]] = 1
        directed_num[tmp[i + 1]] += 1

print(*solve(seq, directed_num), sep='\n')
