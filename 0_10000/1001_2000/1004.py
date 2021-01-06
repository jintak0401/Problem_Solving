from sys import stdin

input = stdin.readline


def solve():
    arr, brr = set(), set()
    pos = list(map(int, input().split()))
    a, b = tuple(pos[:2]), tuple(pos[2:])

    def is_inside(t, x, y, r):
        return (x - t[0]) ** 2 + (y - t[1]) ** 2 < r ** 2

    for i in range(int(input())):
        x, y, r = map(int, input().split())
        if is_inside(a, x, y, r): arr.add(i)
        if is_inside(b, x, y, r): brr.add(i)

    return len(arr ^ brr)


for _ in range(int(input())):
    print(solve())
