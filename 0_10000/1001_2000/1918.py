ans = ''

def all_pop(stack, bracket, mul):
    global ans
    while len(stack) > 0:
        tmp = stack.pop()
        if mul and (tmp == '+' or tmp == '-'):
            stack.append(tmp)
            return
        if tmp == '(' and bracket:
            return
        elif tmp == '(':
            stack.append('(')
            return
        else:
            ans += tmp


exp = input()

index = 0

stack = []

ans = ''

while index < len(exp):
    
    oper = exp[index]

    if oper == '+' or oper == '-':
        all_pop(stack, False, False)
        stack.append(oper)

    elif oper == '(':
        stack.append(oper)

    elif oper == '*' or oper == '/':
        if len(stack) > 0 and (stack[-1] == '*' or stack[-1] == '/'):
            all_pop(stack, False, True)
        stack.append(oper)

    elif oper == ')':
        all_pop(stack, True, False)

    else:
        ans += oper

    index += 1

all_pop(stack, False, False)

print(ans)

