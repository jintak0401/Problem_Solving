from sys import stdin

input = stdin.readline

def get_xor(a, b):

    return (a & ~b) | (b & ~a)


domino_num, quest_num = map(int, input().split())

domino = list(map(int, input().split()))

xor = [0 for _ in range(domino_num)]
xor[1] = domino[0]

for i in range(2, domino_num):
    xor[i] = get_xor(xor[i - 1], domino[i - 1])

for _ in range(quest_num):

    quest = list(map(int, input().split()))
    x = quest[1] - 1
    y = quest[2] - 1

    if quest[0] == 0:
        print(get_xor(xor[x], xor[y]))

    else:
        tmp_xor = get_xor(xor[x], xor[y])
        val = quest[3]
        print((tmp_xor & ~val) | (val & ~tmp_xor))


