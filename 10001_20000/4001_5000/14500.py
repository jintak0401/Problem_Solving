height, width = map(int, input().split())

max_sum = -1;

mat = []

for i in range(height):
    mat.append(list(map(int, input().split())))


#
#
#
#
for i in range(height - 3):
    for j in range(width):
        sum_val = 0
        for k in range(4):
            sum_val += mat[i + k][j]
        if max_sum < sum_val:
            max_sum = sum_val


# print('\n\n#\n#\n#\n#')
# print('\n%d\n\n'%max_sum)

# # # #
for i in range(width - 3):
    for j in range(height):
        sum_val = 0
        sum_val = sum(mat[j][i:i+4])
        if max_sum < sum_val:
            max_sum = sum_val

# print('# # # #')
# print('\n%d\n\n'%max_sum)

# #
#
#
for i in range(height - 2):
    for j in range(width - 1):
        tmp_sum = [0, 0, 0]
        part_sum = 0
        for k in range(3):
            part_sum += mat[i+k][j]
        for k in range(3):
           tmp_sum[k] = part_sum + mat[i + k][j + 1]
        if max_sum < max(tmp_sum):
            max_sum = max(tmp_sum)



# print('# #\n#\n#')
# print('\n%d\n\n'%max_sum)


# #
  # 
  #
for i in range(height - 2):
    for j in range(1, width):
        tmp_sum = [0, 0, 0]
        part_sum = 0
        for k in range(3):
            part_sum += mat[i+k][j]
        for k in range(3):
            tmp_sum[k] = part_sum + mat[i + k][j - 1]
        if max_sum < max(tmp_sum):
            max_sum = max(tmp_sum)

# print('# #\n  #  #')
# print('\n%d\n\n'%max_sum)

# # #
#
for i in range(height - 1):
    for j in range(width - 2):
        tmp_sum = [0, 0, 0]
        part_sum = 0
        for k in range(3):
            part_sum += mat[i][j + k]
        for k in range(3):
            tmp_sum[k] = part_sum + mat[i + 1][j + k]
        if max_sum < max(tmp_sum):
            max_sum = max(tmp_sum)


# print('# # #\n#')
# print('\n%d\n\n'%max_sum)

#
# # #
for i in range(1, height):
    for j in range(width - 2):
        tmp_sum = [0, 0, 0]
        part_sum = 0
        for k in range(3):
            part_sum += mat[i][j + k]
        for k in range(3):
            tmp_sum[k] = part_sum + mat[i - 1][j + k]
        if max_sum < max(tmp_sum):
            max_sum = max(tmp_sum)

# print('#\n# # #')
# print('\n%d\n\n'%max_sum)

  # #
# #
for i in range(height - 1):
    for j in range(width - 1):
        tmp_sum = [0, 0, 0] 
        part_sum = sum(mat[i][j:j+2])
        for k in range(j - 1, j + 2):
            if 0 <= k <= width - 2:
                tmp_sum[k - j + 1] = part_sum + sum(mat[i + 1][k : k + 2])
        if max_sum < max(tmp_sum):
            max_sum = max(tmp_sum)

# print('  # #\n# #')
# print('\n%d\n\n'%max_sum)

#
# #
  #
for i in range(height - 1):
    for j in range(width - 1):
        tmp_sum = [0, 0, 0]
        part_sum = 0
        for k in range(2):
            part_sum += mat[i + k][j]
        for k in range(i - 1, i + 2):
            if 0 <= k <= height - 2:
                tmp_sum[k - i + 1] = part_sum
                for l in range(2):
                    tmp_sum[k - i + 1] += mat[k + l][j + 1]

        if max_sum < max(tmp_sum):
            max_sum = max(tmp_sum)

# print('#\n# #\n  #')
# print('\n%d\n\n'%max_sum)


print(max_sum)

