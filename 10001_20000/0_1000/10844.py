def solve(n):

    arr = [[0 for _ in range(n)] for _ in range(10)]
    for i in range(10):
        arr[i][0] = 1
    
    for i in range(1, n):
        for j in range(10):
            if j > 0:
                arr[j][i] += arr[j - 1][i - 1]
            if j < 9:
                arr[j][i] += arr[j + 1][i - 1]

    sum_val = 0
    for i in range(1, 10):
        sum_val += arr[i][-1]
    return sum_val % 1000000000


print(solve(int(input())))

