from sys import stdin
input = stdin.readline

def solve():
    N = int(input())
    arr = [tuple(map(int, input().split())) for _ in range(N)]
    arr.sort(key = lambda x : x[1])
    ans = 10 ** 10
    
    t = 0
    for i in range(N):
        t += arr[i][0]
        ans = min(ans, arr[i][1] - t)

    print(ans if ans >= 0 else -1)
    return

solve()
