rows,columns = input().split()
rows,columns = int(rows),int(columns)
a = []
count = 0
for i in range(rows):
    helper = input().split()
    a.append(helper)
for i in range(rows):
    for j in range(columns):
        a[i][j] = int(a[i][j])
 
#print(a)
blobs = []
 
 
def type_1(matrix):
    global count
    for i in range(rows):
        for j in range(columns):
            try:
                if (matrix[i][j] != 0) and (matrix[i+1][j] != 0) and (matrix[i+1][j+1] != 0):
                    x1 = [i,j]
                    x2 = [i+1,j]
                    x3 = [i+1,j+1]
                    blobs.append([x1,x2,x3])
            except IndexError:
                pass
    for one_blob in blobs:
        if x1_valid(matrix,one_blob[0][0],one_blob[0][1]) is True and x2_valid(matrix,one_blob[1][0],one_blob[1][1]) is True and x3_valid(matrix,one_blob[2][0],one_blob[2][1]) is True:
            matrix[one_blob[0][0]][one_blob[0][1]] = 0
            matrix[one_blob[1][0]][one_blob[1][1]] = 0
            matrix[one_blob[2][0]][one_blob[2][1]] = 0
            count+=1
 
    for g in matrix:
        print(*g)
    print(count)
 
 
 
def x1_valid(matrix,i,j):
    check1 = True
    check2 = True
    check3 = True
    check4 = True
    check5 = True
    try:
        if i-1 < 0 or j-1 < 0:
            raise IndexError
        elif matrix[i-1][j-1] == 0:
            raise IndexError
        else:
            check1 = False
    except IndexError:
        check1 = True
 
    try:
        if i-1 < 0:
            raise IndexError
        elif matrix[i-1][j] == 0:
            raise IndexError
        else:
            check2 = False
    except IndexError:
        check2 = True
 
    try:
        if j-1 < 0:
            raise IndexError
        elif matrix[i][j-1] == 0:
            raise IndexError
        else:
            check3 = False
    except IndexError:
        check3 = True
 
    try:
        if i-1 < 0 or j+1 >= len(matrix[0]):
            raise IndexError
        elif matrix[i-1][j+1] == 0:
            raise IndexError
        else:
            check4 = False
    except IndexError:
        check4 = True
 
    try:
        if j+1 >= len(matrix[0]):
            raise IndexError
        elif matrix[i][j+1] == 0:
            raise IndexError
        else:
            check5 = False
    except IndexError:
        check5 = True
 
    if check1 == check2 == check3 == check4 == check5 == True:
        return True
    else:
        return False
 
def x2_valid(matrix,i,j):
    check1 = True
    check2 = True
    check3 = True
    try:
        if j-1 < 0:
            raise IndexError
        elif matrix[i][j-1] == 0:
            raise IndexError
        else:
            check1 = False
    except IndexError:
        check1 = True
 
    try:
        if j-1 < 0 or i+1 >= len(matrix):
            raise IndexError
        elif matrix[i+1][j-1] == 0:
            raise IndexError
        else:
            check2 = False
    except IndexError:
        check2 = True
 
    try:
        if i+1 >= len(matrix):
            raise IndexError
        elif matrix[i+1][j] == 0:
            raise IndexError
        else:
            check3 = False
    except IndexError:
        check3 = True
 
    if check1 == check2 == check3 == True:
        return True
    else:
        return False
 
def x3_valid(matrix,i,j):
    check1 = True
    check2 = True
    check3 = True
    check4 = True
 
    try:
        if i+1 >= len(matrix):
            raise IndexError
        elif matrix[i+1][j] == 0:
            raise IndexError
        else:
            check1 = False
    except IndexError:
        check1 = True
 
    try:
        if i+1 >= len(matrix) or j+1 >= len(matrix[0]):
            raise IndexError
        elif matrix[i+1][j+1] == 0:
            raise IndexError
        else:
            check2 = False
    except IndexError:
        check2 = True
 
    try:
        if j+1 >= len(matrix[0]):
            raise IndexError
        elif matrix[i][j+1] == 0:
            raise IndexError
        else:
            check3 = False
    except IndexError:
        check3 = True
 
    try:
        if i-1 < 0 or j+1 >= len(matrix[0]):
            raise IndexError
        elif matrix[i-1][j+1] == 0:
            raise IndexError
        else:
            check4 = False
    except IndexError:
        check4 = True
 
    if check1 == check2 == check3 == check4 == True:
        return True
    else:
        return False
 
 
 
 
 
 
 
type_1(a)