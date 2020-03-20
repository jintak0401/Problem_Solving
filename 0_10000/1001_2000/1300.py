def get_num(size, num):

    start, end = 0, 0

    for i in range(1, size + 1):
        if i > num:
            break
        else:
            if i * size < num:
                start += size
            else:
                start += (num // i)
                if num % i == 0:
                    start -= 1
                    end += 1
        
    return start + 1, end + start




def get_ans(size, pos):


    head, tail = 1, size ** 2

    while head <= tail:

        mid = (head + tail) // 2

        start, end = get_num(size, mid)

        if start <= pos <= end:
            return mid
        elif pos < start:
            tail = mid - 1
        else:
            head = mid + 1


size = int(input())
pos = int(input())

# mat = [i * j for i in range(1, size + 1)
        # for j in range(1, size + 1)]

# mat.sort()


# for i in range(1, size + 1):
    # for j in range(1, size + 1):
        # print('%3d'%(i * j), end = ' ')
    # print()

print(get_ans(size, pos))

# for i in range(1, len(mat) + 1):
    # ans = get_ans(size, i)
    # if not ans:
        # print(i)
    # if mat[i - 1] != ans:
            # print('=============================')
            # print('정답 : {0} 번째  ==> {1} ( {2} ~ {3} )'.format(i, mat[i - 1], mat.index(mat[i - 1]) + 1, mat.index(mat[i - 1]) + mat.count(mat[i-1])))
            # start, end = get_num(size, mat[i - 1])
            # print('오답 : {0} 번째  ==> {1} ( {2} ~ {3} )'.format(i, ans, start, end))
            # print('=============================')

