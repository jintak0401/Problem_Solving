from sys import stdin

input = stdin.readline

def func(arr, n, m):
    d = ((0, 1), (0, -1), (1, 0), (-1, 0))


    check = [[[True for _ in range(m)] for _ in range(n)] for _ in range(2)]
    q = [(0, 0, 1)]
    step = 1
    tmp = []

    while q:

        x, y, can_crash = q.pop()

        if x == n - 1 and y == m - 1:
            return step

        for dx, dy in d:

            pos_x = x + dx
            pos_y = y + dy

            if 0 <= pos_x < n and 0 <= pos_y < m:

                if arr[pos_x][pos_y] == '1':

                    if can_crash and check[can_crash][pos_x][pos_y]:
                        tmp.append((pos_x, pos_y, 0))
                        check[can_crash][pos_x][pos_y] = False

                else:

                    if check[can_crash][pos_x][pos_y]:
                        tmp.append((pos_x, pos_y, can_crash))
                        check[can_crash][pos_x][pos_y] = False


        if not q:
            step += 1
            q.extend(tmp)
            tmp.clear()

    return -1


n, m = map(int, input().split())

arr = [input().rstrip() for _ in range(n)]

print(func(arr, n, m))

