import sys

inf = float('inf')

# def printing(city, path):
    # print('========================================')
    # for i in range(1, len(city)):
        # for j in range(1, len(city)):
            # if city[i][j] == inf:
                # print('inf ', end = ' ')
            # else:
                # digit = 4 - city[i][j] // 10
                # print(city[i][j], end = ' ' * digit) 
        # print()
    # print()
    # print()
    # for i in range(1, len(city)):
        # for j in range(1, len(city)):
            # print('NIL' if path[i][j] == -1 else ' %d '%(path[i][j]), end = ' ')
        # print()
    # print('========================================')

# def floyd(city, path):
def floyd(city):
    for i in range(1, len(city)):
        # printing(city, path)
        for j in range(1, len(city)):
            for k in range(1, len(city)):
                if j != i and k != i:
                    val = city[i][k] + city[j][i]
                    if val < city[j][k]:
                        city[j][k] = val
                        # path[j][k] = path[i][k]

    for i in range(1, len(city)):
        for j in range(1, len(city)):
            if city[i][j] == inf:
                city[i][j] = 0
                        

city_num = int(sys.stdin.readline())
bus_num = int(sys.stdin.readline())

city = [[inf if i != j else 0 for i in range(city_num + 1)]
        for j in range(city_num + 1)]

# path = [[-1 for i in range(city_num + 1)] for j in range(city_num + 1)]

for i in range(bus_num):
    start, end, weight = map(int, sys.stdin.readline().split())
    city[start][end] = min(weight, city[start][end])
    # path[start][end] = start

# floyd(city, path)
floyd(city)

for i in range(city_num):
    print(' '.join(map(str, city[i + 1][1:])))

# for i in range(city_num):
    # print(' '.join(map(str, path[i + 1][1:])))

