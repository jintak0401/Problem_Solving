def solve(length):
    
    arr = [[[0 for _ in range(1 << 10)] for _ in range(10)] for _ in range(length)]
    
    for i in range(1, 10):
        arr[0][i][1 << i] = 1

    for i in range(1, length):
        for j in range(10):
            for k in range(1 << 10):
                bit = k | (1 << j)
                if j > 0:
                    arr[i][j][bit] += arr[i - 1][j - 1][k]
                if j < 9:
                    arr[i][j][bit] += arr[i - 1][j + 1][k]

    sum_val = 0
    for i in range(10):
        sum_val += arr[-1][i][(1 << 10) - 1]

    return sum_val % 1000000000


print(solve(int(input())))
