import sys

ans = []
code_length = 0

def check_condition(code):
    count1 = code.count('a') + code.count('e') + code.count('i') + code.count('o') + code.count('u')
    count2 = len(code) - count1
    if count1 >= 1 and count2 >= 2:
        return True
    else:
        return False

def get_ans(letter, pos, code):

    if len(code) == code_length and check_condition(code):
        ans.append(code) 
        return
    elif len(code) < code_length:
        origin = code
        remain_length = code_length - len(code)
        for i in range(pos, len(letter) - remain_length + 1):
            tmp_code = origin + letter[i]
            get_ans(letter, i + 1, tmp_code)




code_length, letter_length = map(int, sys.stdin.readline().split())

letter = list(sys.stdin.readline().split())

letter.sort()

get_ans(letter, 0, '')

print('\n'.join(ans))

