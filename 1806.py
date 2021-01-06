from sys import stdin

input = stdin.readline

def solve():

    N, S = map(int, input().split())

    arr = list(map(int, input().split()))

    inf = float('inf')
    left, sum_val, ans= 0, 0, inf

    for right in range(N):
        sum_val += arr[right]
        while sum_val - arr[left] >= S:
            sum_val -= arr[left]
            left += 1

        if sum_val >= S and ans > right - left:
            ans = right - left + 1

    print(ans if ans != inf else 0)
    return

solve()
