def make_quad(mat):

    ans = ''
    
    if is_one_color(mat):
        return str(mat[0][0])
    else:
        half = len(mat) // 2
        ans += '('
        for i in range(2):
            for j in range(2):
                tmp = []
                for k in range(half):
                    tmp.append(mat[i * half + k][half * j : half * (j + 1)])

                ans += make_quad(tmp)

        ans += ')'
        return ans

                    

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
    mat.append(list(map(int, input())))

ans = ''
ans += make_quad(mat)

print(ans)
