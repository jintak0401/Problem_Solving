from sys import stdin
input = stdin.readline


def get_sum(arr):
    lu = [[0] * len(arr) for _ in range(len(arr))]
    ld = [[0] * len(arr) for _ in range(len(arr))]
    ru = [[0] * len(arr) for _ in range(len(arr))]
    rd = [[0] * len(arr) for _ in range(len(arr))]

    for i in range(1, len(arr) - 1):
        for j in range(1, len(arr[i]) - 1):
            lu[i][j] = lu[i][j-1] + lu[i-1][j] - lu[i-1][j-1] + arr[i][j]
            ld[-i-1][j] = ld[-i-1][j-1] + ld[-i][j] - ld[-i][j-1] + arr[-i-1][j]
            ru[i][-j-1] = ru[i-1][-j-1] + ru[i][-j] - ru[i-1][-j] + arr[i][-j-1]
            rd[-i-1][-j-1] = rd[-i][-j-1] + rd[-i-1][-j] - rd[-i][-j] + arr[-i-1][-j-1]

    return lu, ld, ru, rd

def solve(arr):
   
    lu, ld, ru, rd = get_sum(arr)
    ans = 0

    for i in range(1, len(arr)):
        for j in range(1, len(arr[i])):
            if 0 < i < len(arr) - 1 and j < len(arr) - 1 and lu[i][j] == rd[i+1][j+1]:
                ans += 1
            if i > 0 and 



size = int(input())
arr = [[0] * (size + 2)]
for _ in range(size):
    arr.append([0] + list(map(int, input().split())) + [0])
arr.append([0] * (size + 2))

print('----------------')
for i in arr:
    print(*i)

lu, ld, ru, rd = get_sum(arr)

tmp = [lu, ld, ru, rd]

print('===============')
for k in range(4):
    for i in range(len(arr)):
        for j in range(len(arr)):
            print(tmp[k][i][j], end =' ')
        print()
    print('===================')
