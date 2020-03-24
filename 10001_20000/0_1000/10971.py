from sys import stdin

def get_digit(num):
    ret_val = 0
    while num & 1 == 0:
        ret_val += 1
    return ret_val

def tsp(dist):

    visited_all = (1 << len(dist)) - 1
    inf = float('inf')

    dp = [[None] * (1 << len(dist)) for _ in range(len(dist))]

    def find_path(last, visited):

        if visited == visited_all:
            return dist[last][0] or inf
        
        elif dp[last][visited] is not None:
            return dp[last][visited]

        else:
            tmp = inf

            for city in range(len(dist)):
                if visited & (1 << city) == 0 and dist[last][city] != 0:
                    tmp = min(tmp, find_path(city, visited | (1 << city)) + dist[last][city])
            dp[last][visited] = tmp
            return tmp

    return find_path(0, 1 << 0)


input = stdin.readline

dist = []

city_num = int(input())
for _ in range(city_num):
    dist.append(list(map(int, input().split())))

print(tsp(dist))
