from sys import stdin
input = stdin.readline

def solve(n):
    arr = list(map(int, input().split()))
    ans = []
    for i in range(len(arr) - 1, -1, -1):
        ans.insert(arr[i], i + 1)
    return ans

print(*solve(int(input())))