from sys import stdin

input = stdin.readline

def solve():
    T = int(input())
    for _ in range(T):
        N = int(input())
        arr = list(map(int, input().split()))

        inf = float('inf')
        dp = [[inf] * N for _ in range(N)]
        sum_val = [[0] * N for _ in range(N)]
        for i in range(N):
            sum_val[i][i] = arr[i]
            for j in range(i + 1, N):
                sum_val[i][j] = sum_val[i][j - 1] + arr[j]

        for i in range(N):
            dp[i][i] = arr[i]

        for i in range(N - 1):
            for j in range(N - i - 1):
                for k in range(j, i + j + 1):
                    left = dp[j][k] if j != k else 0
                    right = dp[k + 1][i + j + 1] if k != i + j else 0
                    if dp[j][i + j + 1] > left + right + sum_val[j][i + j + 1]:
                        dp[j][i + j + 1] = left + right + sum_val[j][i + j + 1]

        print(dp[0][-1])

    return

solve()
