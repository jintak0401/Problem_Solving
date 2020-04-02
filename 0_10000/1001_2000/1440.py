a, b, c = map(int, input().split(':'))
ans = 0

if a >= 60 or b >= 60 or c >= 60:
    pass

elif a == b == c:
    if 1 <= a <= 12:
        ans = 6

else:

    if a == b and b != c:
        if 1 <= a <= 12:
            ans = 4
        if 1 <= c <= 12:
            ans += 2

    elif a == c and c != b:
        if 1 <= a <= 12:
            ans = 4
        if 1 <= b <= 12:
            ans += 2

    elif b == c and c != a:
        if 1 <= b <= 12:
            ans = 4
        if 1 <= a <= 12:
            ans += 2

    elif 1 <= a <= 12 and 1 <= b <= 12 and 1 <= c <= 12:
        ans = 6
    elif 1 <= a <= 12 and 1 <= b <= 12 and (not 1 <= c <= 12):
        ans = 4
    elif 1 <= a <= 12 and (not 1 <= b <= 12) and 1 <= c <= 12:
        ans = 4
    elif 1 <= a <= 12 and (not 1 <= b <= 12) and (not 1 <= c <= 12):
        ans = 2
    elif (not 1 <= a <= 12) and 1 <= b <= 12 and 1 <= c <= 12:
        ans = 4
    elif (not 1 <= a <= 12) and 1 <= b <= 12 and (not 1 <= c <= 12):
        ans = 2
    elif (not 1 <= a <= 12) and (not 1 <= b <= 12) and 1 <= c <= 12:
        ans = 2
    elif (not 1 <= a <= 12) and (not 1 <= b <= 12) and (not 1 <= c <= 12):
        ans = 0

print(ans)
