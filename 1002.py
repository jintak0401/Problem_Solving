from sys import stdin
from decimal import Decimal

case_num = int(input())

for _ in range(case_num):

    x1, y1, r1, x2, y2, r2 = map(Decimal, input().split())

    if x1 == x2 and y1 == y2:
        if r1 == r2:
            print(-1)
        else:
            print(0)
        
    else:
        dist = ((x1 - x2) ** Decimal('2') + (y1 - y2) ** Decimal('2')) ** Decimal('0.5')

        if dist > r1 + r2:
            print(0)

        elif dist == r1 + r2:
            print(1)

        else:
            if dist == abs(r1 - r2):
                print(1)
            elif dist < abs(r1 - r2):
                print(0)
            else:
                print(2)
