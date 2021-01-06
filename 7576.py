from sys import stdin
import collections

def checking_all_one(mat):
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            if mat[i][j] == 0:
                return False
    return True

def insert_queue(q, mat, x, y):

    index = [[x, y - 1], [x, y + 1], [x - 1, y], [x + 1, y]]

    pos = []
    j = 0
    while j < len(index):
        tmp = index[j]
        if (0 <= tmp[0] < len(mat) and 0 <= tmp[1] < len(mat[0])):
            pos.append(tmp)
        j += 1

    for i in pos:
        if mat[i[0]][i[1]] == 0:
            q.append(i)
            mat[i[0]][i[1]] = 1

col, row = map(int, stdin.readline().split())

q = collections.deque([])

mat = []
for i in range(row):
    mat.append(list(map(int, stdin.readline().split())))

    for j in range(col):
        if mat[i][j] == 1:
            q.append([i, j])

ans = 0

while len(q):
    ans += 1
    init_len = len(q)

    for i in range(init_len):
        pos = q.popleft()
        insert_queue(q, mat, *pos)

if checking_all_one(mat):
    print(ans - 1)
else:
    print(-1)


