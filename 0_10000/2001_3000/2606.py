def find(mat, x):

    if mat[x] > 0:
        x = find(mat, mat[x])
    return x

def union(mat, a, b):

    a = find(mat, a)
    b = find(mat, b)

    if (a == b):
        return

    elif mat[a] < mat[b]:
        mat[b] = a
    else:
        if mat[a] == mat[b]:
            mat[a] -= 1
        mat[b] = a



length = int(input())
connect = int(input())

mat = [0] * (length + 1)

for i in range(connect):
    union(mat, *list(map(int, input().split())))

num = 0

for i in range(2, length + 1):
    if find(mat, i) == find(mat, 1):
        num += 1

print(num)

