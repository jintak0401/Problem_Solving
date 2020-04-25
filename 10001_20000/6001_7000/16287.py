from sys import stdin
input = stdin.readline

def solve():

    weight, length = map(int, input().split())
    arr = sorted(map(int, input().split()))
    tmp = weight - 2
    weights = [0] * (weight + 1)
    for i in range(length):
        for j in range(i + 1, length):
            sth1 = arr[i]
            sth2 = arr[j]
            if sth1 + sth2 < tmp:
                weights[sth1 + sth2] = sth1

    for i in range(3, weight // 2 + 1):
        sth1 = weights[i]
        sth2 = weights[weight - i]
        if sth1 != 0 and sth2 != 0:  # 무게의 합이 i 인 것 중 무거운 것의 무게 < 무게의 합이 weight - i 인 것중 가벼운 것의 무게
            if i - sth1 < sth2:
                print("YES")
                return
    print("NO")

solve()
