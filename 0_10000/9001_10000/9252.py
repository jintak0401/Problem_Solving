def get_mat(a, b):
    mat = [[0 for i in range(len(a) + 1)] for j in range(len(b) + 1)]
    direction = [[0 for i in range(len(a) + 1)] for j in range(len(b) + 1)]

    for i in range(1, len(mat)):
        for j in range(1, len(mat[0])):
            if a[j - 1] == b[i - 1]:
                mat[i][j] = mat[i - 1][j - 1] + 1
            elif mat[i - 1][j] < mat[i][j - 1]:
                direction[i][j] = -1
                mat[i][j] = mat[i][j - 1]
            else:
                direction[i][j] = 1
                mat[i][j] = mat[i - 1][j]

    return mat, direction


a = input()
b = input()

mat, direction = get_mat(a, b)

index = mat[-1][-1]

print(index)

ans = ''

a_pos = len(a)
b_pos = len(b)

while index > 0:

    val = direction[b_pos][a_pos]

    if val == 0:
        index -= 1
        ans = a[a_pos - 1] + ans
        a_pos -= 1
        b_pos -= 1

    elif val == 1:
        b_pos -= 1
    
    else:
        a_pos -= 1


print(ans)
