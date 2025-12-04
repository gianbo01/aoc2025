from get_data import get_data, answer

matrix = ["..@@.@@@@.",
        "@@@.@.@.@@",
        "@@@@@.@.@@",
        "@.@@@@..@.",
        "@@.@@@@.@@",
        ".@@@@@@@.@",
        ".@.@.@.@@@",
        "@.@@@.@@@@",
        ".@@@@@@@@.",
        "@.@.@@@.@."]

matrix = get_data(4).splitlines()
matrix = [list(row) for row in matrix]

def part1(matrix):
    l_row = len(matrix[0])
    l_col = len(matrix)
    tot = 0
    
    for j in range(l_col):
        for i in range(l_row):
            count = 0
            if matrix[i][j] == "@":
                count = count+1 if j>0 and matrix[i][j-1] == "@" else count
                count = count+1 if j<l_row-1 and matrix[i][j+1] == "@" else count

                count = count+1 if i>0 and matrix[i-1][j] == "@" else count
                count = count+1 if i>0 and j>0 and matrix[i-1][j-1] == "@" else count
                count = count+1 if i>0 and j<l_row-1 and matrix[i-1][j+1] == "@" else count

                count = count+1 if i<l_col-1 and matrix[i+1][j] == "@" else count
                count = count+1 if i<l_col-1 and j>0 and matrix[i+1][j-1] == "@" else count
                count = count+1 if i<l_col-1 and j<l_row-1 and matrix[i+1][j+1] == "@" else count

                if count < 4:
                    tot += 1

    return tot

def find_replace(matrix):
    l_row = len(matrix[0])
    l_col = len(matrix)
    tot = 0
    replace = []
    
    for j in range(l_col):
        for i in range(l_row):
            count = 0
            if matrix[i][j] == "@":
                #print("i, j", i,j)
                count = count+1 if j>0 and matrix[i][j-1] == "@" else count
                count = count+1 if j<l_row-1 and matrix[i][j+1] == "@" else count

                count = count+1 if i>0 and matrix[i-1][j] == "@" else count
                count = count+1 if i>0 and j>0 and matrix[i-1][j-1] == "@" else count
                count = count+1 if i>0 and j<l_row-1 and matrix[i-1][j+1] == "@" else count

                count = count+1 if i<l_col-1 and matrix[i+1][j] == "@" else count
                count = count+1 if i<l_col-1 and j>0 and matrix[i+1][j-1] == "@" else count
                count = count+1 if i<l_col-1 and j<l_row-1 and matrix[i+1][j+1] == "@" else count

                if count < 4:
                    tot += 1
                    replace.append((i,j))

    for k in replace:
        matrix[k[0]][k[1]] = "."
    return tot


def part2(matrix):
    tot = 0
    flag = True
    while flag:
        tmp = find_replace(matrix)
        flag = False if tmp == 0 else True
        tot += tmp
    return tot

print(answer(part1(matrix), 1, 4))

print(answer(part2(matrix), 2, 4))