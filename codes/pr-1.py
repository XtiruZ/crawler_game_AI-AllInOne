rows = 3
cols=6
#// create 二維列表
matrix = [[0 for col in range(cols)] for row in range(rows)]

for i in range(rows):
    for j in range(cols):
        matrix[i][j] = i*3+j
        print(matrix[i][j], end=',')
    print('\n')

    