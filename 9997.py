from sys import stdin

ans = 0

def OR(arr):
    ret_val = 0
    for i in arr:
        ret_val |= i
    return ret_val


def func(arr, letter):
    global ans

    if letter == compare:
        ans += 2 ** len(arr)
        return
    
    else:
        if (letter | OR(arr[1:])) == compare:
            func(arr[1:], letter)
        if ((letter | arr[0]) | OR(arr[1:])) == compare:
            func(arr[1:], letter | arr[0])


input = stdin.readline
length = int(input())

arr = []
compare = (1 << 26) - 1
check = 0

for _ in range(length):
    user_input = input().rstrip()
    num = 0
    for i in range(len(user_input)):
        num |= 1 << (ord(user_input[i]) - ord('a'))

    arr.append(num)
    check |= num

if check == compare:
    letter = 0
    func(arr, letter)

print(ans)

