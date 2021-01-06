from sys import stdin

def get_area(pt):

    front = 0
    behind = 0

    length = len(pt)
    for i in range(length):
        front += pt[i % length][0] * pt[(i + 1) % length][1]

    for i in range(length):
        behind += pt[(i + 1) % length][0] * pt[i % length][1]

    area = (front - behind) * 0.5

    return area if area > 0 else -area

input = stdin.readline

length = int(input())

point = [list(map(int, input().split())) for _ in range(length)]


base_pt = point[0]

area = get_area(point)

print('%.1f'%(area))
