from sys import stdin
from collections import deque
input = stdin.readline

seq = 0
group_num = 0
s = []
SSC = []

def dfs(node):
    global grouo, seq, s, arr, discover, group_num

    discover[node] = seq; seq += 1
    ret_val = discover[node]
    s.append(node)

    for i in range(len(arr)):
        if arr[node][i] == '1':
            if discover[i] == -1:
                ret_val = min(ret_val, dfs(i))
            elif group[i] == -1:
                ret_val = min(ret_val, discover[i])

    if ret_val == discover[node]:
        tmp = []
        while True:
            tmp.append(s.pop()) 
            group[tmp[-1]] = group_num
            if tmp[-1] == node:
                break
        group_num += 1
        SSC.append(tmp)
    return ret_val
        
size = int(input())
cost = list(map(int, input().split()))
arr = []
group = [-1 for _ in range(size)]
for _ in range(size):
    arr.append(list(input().rstrip()))

discover = [-1 for _ in range(size)]
for i in range(size):
    if discover[i] == -1:
        dfs(i)

ans = 0
for i in range(len(SSC)):
    ans += min([cost[j] for j in SSC[i]])

print(ans)
