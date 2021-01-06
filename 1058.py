from sys import stdin
input = stdin.readline

def solve():

    size = int(input())
    friend = [set() for _ in range(size)]
    for i in range(size):
        tmp = list(input().rstrip())
        for j in range(len(tmp)):
            if tmp[j] == 'Y':
                friend[i].add(j)

    ans = 0
    for i in range(size):
        tmp = set()
        for j in friend[i]:
            tmp |= (friend[j] - {i})
        ans = max(len(tmp | friend[i]), ans)

    print(ans)

solve()
