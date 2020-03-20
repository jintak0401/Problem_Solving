def make_star(size):
    if size == 0:
        return [[' ', ' ', '*', ' ', ' '], [' ', '*', ' ', '*', ' '], ['*', '*', '*', '*', '*']]
    else:
        star = [[' ' for i in range(6 * (2 ** size) - 1)] for j in range(6 * (2 ** (size - 1)))]
        part = make_star(size - 1)

        point = []
        point.append([0, len(star[0]) // 2])
        point.append([len(star) // 2, len(star[0]) // 4])
        point.append([len(star) // 2, 3 * len(star[0]) // 4])

        arr_len = len(part[0]) // 2
        for i in range(3):
            for j in range(len(part)):
                star[point[i][0] + j][point[i][1] - j : point[i][1] + j + 1] = part[j][arr_len - j:arr_len + j + 1]

        return star


size = int(input())

size_mat = [3 * (2 ** i) for i in range(11)]

size = size_mat.index(size)

star = make_star(size)

for i in range(len(star)):
    print(''.join(star[i]))
