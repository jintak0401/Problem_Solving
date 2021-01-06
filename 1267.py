from sys import stdin

input = stdin.readline

dic = {}

n, m = map(int, input().split())

arr = []

for _ in range(n):
    arr.append(list(map(int, input().split())))

case_num = int(input())

for _ in range(case_num):
    i, j, x, y = map(int, input().split())
    i -= 1
    j -= 1
    x -= 1
    y -= 1

    ans = 0
    if (i, j, x, y) in dic:
        ans = dic[(i, j, x, y)]

    else:
        for k in range(i, x + 1):
            if (k, j, k, y) not in dic:
                dic[(k, j, k, y)] = sum(arr[k][j:y+1])
            val = dic[(k, j, k, y)]
            ans += val
            # dic[(i, j, k, y)] = ans

    
    print(ans)


