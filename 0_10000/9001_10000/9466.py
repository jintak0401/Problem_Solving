from sys import stdin, setrecursionlimit as SRL
SRL(10 ** 6)
input = stdin.readline

target = None
ans = 0
confirmed = []
partner = []
def dfs(idx):

    global ans, target, confirmed, partner

    if confirmed[idx] == 2:
        return

    elif confirmed[idx] == 1:
        target = idx
        ans += 1
    else:
        confirmed[idx] = 1
        dfs(partner[idx])
        confirmed[idx] = 2

        if target != None:
            if target == idx:
                target = None
            else:
                ans += 1

case_num = int(input())
for _ in range(case_num):
    num = int(input())
    partner = [0] + list(map(int, input().split()))
    confirmed = [0 for _ in range(num + 1)]
    for i in range(1, num + 1):
        dfs(i)
    print(num - ans)
    ans = 0
