from sys import stdin
from collections import defaultdict
input = stdin.readline

area = []

def set_area(arr):
    global area
    lu = [[0] * len(arr) for _ in range(len(arr))]
    ld = [[0] * len(arr) for _ in range(len(arr))]
    ru = [[0] * len(arr) for _ in range(len(arr))]
    rd = [[0] * len(arr) for _ in range(len(arr))]

    for i in range(1, len(arr) - 1):
        for j in range(1, len(arr[i]) - 1):
            lu[i][j] = lu[i][j-1] + lu[i-1][j] - lu[i-1][j-1] + arr[i][j]
            ld[-i-1][j] = ld[-i-1][j-1] + ld[-i][j] - ld[-i][j-1] + arr[-i-1][j]
            ru[i][-j-1] = ru[i-1][-j-1] + ru[i][-j] - ru[i-1][-j] + arr[i][-j-1]
            rd[-i-1][-j-1] = rd[-i][-j-1] + rd[-i-1][-j] - rd[-i][-j] + arr[-i-1][-j-1]

    area = [lu, ld, ru, rd]

def get_area(pt1, pt2, direction):
    if direction == 0:
        return area[0][pt1[0]][pt1[1]] - area[0][pt1[0]][pt2[1] - 1] - area[0][pt2[0] - 1][pt1[1]] + area[0][pt2[0] - 1][pt2[1] - 1]
    elif direction == 1:
        return area[1][pt1[0]][pt1[1]] - area[1][pt1[0]][pt2[1] - 1] - area[1][pt2[0] + 1][pt1[1]] + area[1][pt2[0] + 1][pt2[1] - 1]
    elif direction == 2:
        return area[2][pt1[0]][pt1[1]] - area[2][pt1[0]][pt2[1] + 1] - area[2][pt2[0] - 1][pt1[1]] + area[2][pt2[0] - 1][pt2[1] + 1]
    else:
        return area[3][pt1[0]][pt1[1]] - area[3][pt1[0]][pt2[1] + 1] - area[3][pt2[0] + 1][pt1[1]] + area[3][pt2[0] + 1][pt2[1] + 1]

def solve(arr):
   
    global area
    set_area(arr)
    ans = 0

    for i in range(1, len(arr) - 1):
        for j in range(1, len(arr[i]) - 1):
            tmp_lu = defaultdict(int)
            tmp_ld = defaultdict(int)
            tmp_ru = defaultdict(int)
            tmp_rd = defaultdict(int)
            if i != len(arr) - 2 and j != len(arr) - 2:
                for k in range(1, i + 1):
                    for l in range(1, j + 1):
                        tmp_lu[get_area((i, j), (k, l), 0)] += 1
                for k in range(i + 1, len(arr) - 1):
                    for l in range(j + 1, len(arr) - 1):
                        tmp_rd[get_area((i+1, j+1), (k, l), 3)] += 1
            if i != 1 and j != len(arr) - 2:
                for k in range(len(arr) - 2, i - 1, -1):
                    for l in range(1, j + 1):
                        tmp_ld[get_area((i, j), (k, l), 1)] += 1
                for k in range(i - 1, 0, - 1):
                    for l in range(j + 1, len(arr) - 1):
                        tmp_ru[get_area((i-1, j+1), (k, l), 2)] += 1

            treat, control = [], [] # 실험군, 대조군
            if len(tmp_lu) < len(tmp_rd):
                treat.append(tmp_lu)
                control.append(tmp_rd)
            else:
                treat.append(tmp_rd)
                control.append(tmp_lu)
            if len(tmp_ld) < len(tmp_ru):
                treat.append(tmp_ld)
                control.append(tmp_ru)
            else:
                treat.append(tmp_ru)
                control.append(tmp_ld)

            for k in range(2):
                for key in treat[k].keys():
                    if key in control[k]:
                        ans += control[k][key] * treat[k][key]

    return ans

size = int(input())
arr = [[0] * (size + 2)]
for _ in range(size):
    arr.append([0] + list(map(int, input().split())) + [0])
arr.append([0] * (size + 2))

print(solve(arr))
