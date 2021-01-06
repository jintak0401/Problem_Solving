import sys

a = input()
b = input()

mat = [[0 for i in range(len(a) + 1)] for j in range(len(b) + 1)]

for i in range(1, len(b) + 1):
    for j in range(1, len(a) + 1):
        if a[j - 1] == b[i - 1]:
            mat[i][j] = 1 + mat[i -1][j - 1]
        else:
            mat[i][j] = max(mat[i][j - 1], mat[i - 1][j])

print(mat[-1][-1])

