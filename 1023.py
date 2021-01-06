def checking(ans):
    count = 0
    for i in range(len(ans)):
        if ans[i] == '(':
            count += 1
        else:
            count -= 1
        if count < 0:
            return 1
    return 1 if count != 0 else 0

def middle_checking(ans):
    count = 0
    for i in range(len(ans)):
        if ans[i] == '(':
            count += 1
        else:
            count -= 1
        if count < 0:
            return 1
    return 0

def get_mat(mat, sum_val, pos, length, ans):
    if pos == length:
        ret_val = checking(ans)
        return ret_val

    else:
        if mat[sum_val + length][pos] == -1:
            if sum_val == 0:
                left = get_mat(mat, sum_val + 1, pos + 1, length, ans + '(')
                right = 2 ** (length - pos - 1)
            
            elif sum_val < 0:
                left = 2 ** (length - pos - 1)
                right = left
            else:
                left = get_mat(mat, sum_val + 1, pos + 1, length, ans + '(')
                right = get_mat(mat, sum_val - 1, pos + 1, length, ans + ')')

            mat[sum_val + length][pos] = left + right

        return mat[sum_val + length][pos]

length, seq = map(int, input().split())

seq += 1

mat = [[-1 for i in range(length)] for j in range(2 * length + 1)]


index = 0
sum_val = 0

ans = ''

already = False

a = get_mat(mat, 1, 1, length, ans + '(')
b = get_mat(mat, -1, 1, length, ans + ')')
if (seq > a + b):
    print(-1)
    exit(0)

for i in range(length):

    if middle_checking(ans + '('):
        left = index + 2 ** (length - i - 1)
    else:
        left = index + get_mat(mat, sum_val + 1, i + 1, length, ans + '(')

    if middle_checking(ans + ')'):
        right = left + 2 ** (length - i - 1)
    else:
        right = left + get_mat(mat, sum_val - 1, i + 1, length, ans + ')')

    if seq <= left:
        sum_val += 1
        ans += '('
    else:
        sum_val -= 1
        ans += ')'
        index = left


print(ans)

