import sys

def get_ans(target, val, mat):
    if val == target:
        return 1
    elif val < target:
        if mat[val] == 0:
            ret_val = 0
            ret_val += get_ans(target, val + 1, mat)
            ret_val += get_ans(target, val + 2, mat)
            ret_val += get_ans(target, val + 3, mat)
            mat[val] = ret_val
            return ret_val
        else:
            return mat[val]
    else:
        return 0


num_case = int(sys.stdin.readline())


num = []

for i in range(num_case):
    num.append(int(sys.stdin.readline()))


for i in num:
    mat = [0 for i in range(i + 1)]
    print(get_ans(i, 0, mat))

