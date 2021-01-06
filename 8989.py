import math

def sorting(time, degree):
    for i in range(5):
        for j in range(i + 1, 5):
            if degree[i] > degree[j]:
               time[i], time[j] = time[j], time[i]
               degree[i], degree[j] = degree[j], degree[i]
            elif degree[i] == degree[j]:
                i_time = list(map(int, time[i].split(':')))
                j_time = list(map(int, time[j].split(':')))
                i_time = 60 * i_time[0] + i_time[1]
                j_time = 60 * j_time[0] + j_time[1]
                if i_time > j_time:
                   time[i], time[j] = time[j], time[i]
                   degree[i], degree[j] = degree[j], degree[i]

def get_degree(h, m):
    h %= 12
    # h_degree = 30 * (h + (m / 60))
    h_degree = 30 * h + m / 2
    m_degree = 6 * m

    diff = abs(h_degree - m_degree)

    if diff > 180:
        diff = 360 - diff

    return diff


num_case = int(input())
ans = []

for i in range(num_case):
    time = input().split()
    degree = []
    for j in range(5):
        degree.append(get_degree(*list(map(int, time[j].split(':')))))
    sorting(time, degree)
    ans.append(time[2])

for i in ans:
    print(i)

