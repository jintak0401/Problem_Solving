from sys import stdin

ans = 0

def rotate(sticker):
    
    ret_val = [['0' for _ in range(len(sticker))] for _ in range(len(sticker[0]))]

    for i in range(len(sticker)):
        for j in range(len(sticker[i])):
            ret_val[j][-i - 1] = sticker[i][j]

    return ret_val

def is_fit(arr, x, y, sticker):
    
    for i in range(len(sticker)):
        for j in range(len(sticker[i])):
            if sticker[i][j] == '1' and arr[x + i][y + j] == '1':
                return False

    return True

def attach(arr, x, y, sticker):
    global ans
    for i in range(len(sticker)):
        for j in range(len(sticker[i])):
            if sticker[i][j] == '1':
                arr[x + i][y + j] = '1'
                ans += 1
    

def solve(row, col, sticker):

    global ans
    arr = [['0' for _ in range(col)] for _ in range(row)]

    for st in sticker:
        
        is_attach = False
        for _ in range(4):
            for i in range(row - len(st) + 1):
                for j in range(col - len(st[0]) + 1):
                    if is_fit(arr, i, j, st):
                        attach(arr, i, j, st)
                        is_attach = True
                        break

                if is_attach:
                    break

            if not is_attach:
                st = rotate(st)
            else:
                break


input = stdin.readline

row, col, num = map(int, input().split())

sticker = []

for _ in range(num):
    x, y = map(int, input().split())
    tmp = []
    for _ in range(x):
        tmp.append(input().split())

    sticker.append(tmp)

solve(row, col, sticker)
print(ans)
