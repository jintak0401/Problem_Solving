def draw_line(star, point, length):
    row = point[0]
    col = point[1]
    for i in range(length):
        star[point[0]][col] = 1
        star[row][point[1]] = 1
        if point[2] == 'R':
            col -= 1
            row -= 1
        else:
            col += 1
            row += 1


length = int(input())

if length == 1:
    print('*')

else:

    length = 4 * length - 3

    star = [[0 for i in range(length)] for j in range(length + 2)]
    star[0] = [1 for i in range(length)]
    for i in range(length + 2):
        star[i][0] = 1

    pos = 'R'
    point = [length + 1, length - 1, pos]

    for i in range(length, 2, -2):
        draw_line(star, point, i) 
        if point[2] == 'R':
            point[0] -= (i - 1)
            point[1] -= (i - 3)
            point[2] = 'L'
        else:
            point[0] += (i - 1)
            point[1] += (i - 3)
            point[2] = 'R'

    for i in range(len(star)):
        for j in range(len(star[i])):
            if i == 1 and j == 0:
                print('*', end = '')
                break
            elif star[i][j] == 1:
                print('*', end = '')
            else:
                print(' ', end = '')
        print()

