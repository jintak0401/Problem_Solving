from sys import stdin
input = stdin.readline

def solve():

    m, n = map(int, input().split())
    d = ((-1, 0), (1, 0), (0, -1), (0, 1))
    arr = []

    for _ in range(n):
        arr.append(input().rstrip())

    check = [[False] * m for _ in range(n)]
    
    dic = {'W' : 0, 'B' : 0}
    color = ['W', 'B']
    for k in range(2):
        for i in range(n):
            for j in range(m):
                if arr[i][j] == color[k] and check[i][j] == False:
                    num = 1
                    check[i][j] = True
                    stack = [(i, j)]
                    while stack:
                        nx, ny = stack.pop()
                        for dx, dy in d:
                            x, y = nx + dx, ny + dy
                            if 0 <= x < n and 0 <= y < m:
                                if arr[x][y] == color[k] and check[x][y] == False:
                                    check[x][y] = True
                                    num += 1
                                    stack.append((x, y))
                    dic[color[k]] += num ** 2

    print(dic['W'], dic['B'])
    return

solve()
