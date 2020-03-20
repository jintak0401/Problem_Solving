import sys

global num

def get_ans(mat, x, y, length):

    tmp = mat[x][y]

    if length == 1:
        num[tmp + 1] += 1
        return

    is_one_num = True

    for i in mat[x:x+length]:
        for j in i[y:y+length]:
            if tmp != j:
                is_one_num = False
                break
        if not is_one_num:
            break
    if is_one_num:
        num[mat[x][y] + 1] += 1

    else:
        p = length // 3
        s = 2 * p
        get_ans(mat, x, y, p)
        get_ans(mat, x + p, y, p)
        get_ans(mat, x + s, y, p)
        get_ans(mat, x, y + p, p)
        get_ans(mat, x + p, y + p, p)
        get_ans(mat, x + s, y + p, p)
        get_ans(mat, x, y + s, p)
        get_ans(mat, x + p, y + s, p)
        get_ans(mat, x + s, y + s, p)

    

def is_one_num(mat, x, y, length):
    tmp = mat[x][y]
    for i in range(x, x + length):
        for j in range(y, y + length):
            if tmp != mat[i][j]:
                return False
    return True

size = int(sys.stdin.readline())

num = [0] * 3


mat = [[*map(int, i.split())] for i in sys.stdin]

# mat = []

# for i in range(size):
    # user_input = sys.stdin.readline()
    # mat.append(list(map(int, user_input.split()))) 

get_ans(mat, 0, 0, size)

print('\n'.join(map(str, num)))

