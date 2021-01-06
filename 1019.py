p = []
page = 0

def fill_p(digit):
    for i in range(1, digit):
        p[i] = ((10 ** (i - 1)) * i)

def solve(page):

    if page <= 9:
        return [1 if 1 <= i <= page else 0 for i in range(10)]

    digit = len(str(page))
    ret_val = [p[digit - 1]] * 10

    if digit == 2:
        ret_val[0] -= 1

    else:
        for i in range(1, digit - 1):
            ret_val[0] -= 9 * i * (10 ** (digit - 2 - i))
        ret_val[0] -= digit - 1

    for i in range(digit):
        for j in range(1 if i == 0 else 0, int(str(page)[i])):
            ret_val[j] += 10 ** (digit - i - 1)
        for j in range(10):
            ret_val[j] += p[digit - i - 1] * (int(str(page)[i]) - (1 if i == 0 else 0))
        if i + 1 < digit:
            ret_val[int(str(page)[i])] += int(str(page)[i + 1:]) + 1
        else:
            ret_val[int(str(page)[i])] += 1

    return ret_val

page = int(input())
p = [[0 for _ in range(10)] for _ in range(len(str(page)) + 1)]
p = [0 for _ in range(len(str(page)) + 1)]
fill_p(len(str(page)))
ans = solve(page)
print(' '.join(map(str, ans)))
