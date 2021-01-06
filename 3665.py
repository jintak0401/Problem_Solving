from sys import stdin
from collections import deque

input = stdin.readline

case_num = int(input())

for _ in range(case_num):

    input()

    user_input = list(map(int, input().split()))

    # [in_degree, to_where]
    arr = [0 for _ in range(len(user_input) + 1)] 
    
    for i in range(1, len(arr)):
        arr[user_input[i - 1]] = [i - 1, set(user_input[i:])]

    change_num = int(input())

    for _ in range(change_num):

        # b --> a change to a --> b
        a, b = map(int, input().split())

        if b in arr[a][1]:
            a, b = b, a 

        arr[a][0] -= 1
        arr[a][1] |= {b}
        arr[b][0] += 1
        arr[b][1] -= {a}

    q = deque([])
    ans = []
    
    for i in range(1, len(arr)):
        if arr[i][0] == 0:
            q.append(arr[i])
            ans.append(i)
            break

    while q:

        team = q.popleft()
        
        for i in team[1]:
            arr[i][0] -= 1
            if arr[i][0] == 0:
                q.append(arr[i])
                ans.append(i)


    if len(ans) == len(user_input):
        print(' '.join(map(str, ans)))

    else:
        print("IMPOSSIBLE")
    
