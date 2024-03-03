row_num, col_num = input().split()
row_num = int(row_num)
col_num = int(col_num)
matrix = []
for x in range(row_num):
    matrix.append(list(map(int, input().split())))

transposed_matrix = [list(row) for row in zip(*matrix)]

def top_potential_find(matrix_row):
    if matrix_row[0] == 0 and len(matrix_row) >= 2:
        for element_index in range(len(matrix_row)):
            if matrix_row[element_index] != 0:
                return element_index -1
            elif element_index == len(matrix_row) -1:
                return False
    else:
        return False

def middle_part_exists(start_row,col):
    return matrix[start_row][col] ==0 and matrix[start_row+1][col] ==0 and matrix[start_row+2][col]==0

def bottom_part_exists(row, start_column):
    element1 = matrix[row][start_column]
    element2 = matrix[row][start_column + 1]
    element3 = matrix[row][start_column + 2]
    return element1 == element2 == element3 == 0

def horizontal_valid_check(row_index, start_element,end_element,top_part):
    if top_part:
        if matrix[row_index-1][start_element:end_element+1] == 0 or  matrix[row_index+1][start_element:end_element] ==0:
            return False
        else:
            return True
    else:
        if matrix[row_index-1][start_element+1:end_element+1] == 0 or matrix[row_index+1][start_element:end_element+1]==0:
            return False
        else:
            return True
def vertical_valid_check(start_row,col_index):
    if transposed_matrix[col_index-1][start_row+1:start_row+4] ==0 or transposed_matrix[col_index+1][start_row:start_row+3]==0:
        return False
    else:
        return True
soln_list = []

for row_index in range(len(matrix)):
    if row_index == 0 or row_index == len(matrix) -1:
        pass
    else:
        top_end = top_potential_find(matrix[row_index])#finds the top path and last index of the non zero elemnt
        if horizontal_valid_check(row_index,0,top_end,True):
            middle_part = middle_part_exists(row_index,top_end)
            if middle_part:
                if vertical_valid_check(row_index,top_end):
                    if bottom_part_exists(row_index+3,top_end):
                        if horizontal_valid_check(row_index + 3, top_end, len(matrix[0]) - 1, False):
                            soln_list.append((row_index, top_end))

for list in soln_list:
    print(list[0], list[1])






