def get_ans(mat):
    color = [0, 0]
    if is_one_color(mat):
        color[mat[0][0]] += 1
        return color
    else:

        half = len(mat) // 2

        for i in range(2):
            for j in range(2):
                tmp = []
                for k in range(half):
                    tmp.append(mat[half * i + k][half * j : half * (j + 1)])

                white, black = get_ans(tmp)
                color[0] += white
                color[1] += black

        return color
                

def is_one_color(mat):
    color = mat[0][0]
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            if mat[i][j] != color:
                return False
    
    return True


size = int(input())

mat = []

for i in range(size):
    mat.append(list(map(int, input().split())))


white, black = get_ans(mat)

print(white)
print(black)


