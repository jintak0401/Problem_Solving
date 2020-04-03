from sys import stdin, setrecursionlimit as SRL
SRL(10 ** 5)
input = stdin.readline
dp = []
arr = []

def get_ans(s, e):
    if s > e:
        return 1
    elif dp[s][e] == -1:
        if arr[s] == arr[e] and get_ans(s + 1, e - 1):
            dp[s][e] = 1
        else:
            dp[s][e] = 0
    return dp[s][e]

size = int(input())
arr = ['0'] + input().rstrip().split()
dp = [[-1 if i != j else 1 for i in range(size + 1)] for j in range(size + 1)]
q_num = int(input())
for _ in range(q_num):
    print(get_ans(*map(int, input().split())))
