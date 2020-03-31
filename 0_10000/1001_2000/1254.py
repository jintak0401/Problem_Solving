from sys import stdin

def check(string, i, j):

    while j != len(string):
        if string[i] != string[j]:
            return False
        i -= 1
        j += 1
    return True

    

def solve(string):

    if string == string[::-1]:
        return len(string)
    
    left = len(string) // 2
    
    while True:
        right = left
        if check(string, left, right):
            break
        right += 1

        if check(string, left, right):
            break

        left += 1

    return left + right + 1


input = stdin.readline
print(solve(input().rstrip()))
