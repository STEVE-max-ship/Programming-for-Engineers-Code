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
def type_z(matrix):
    for i in range(rows):
        for j in range(columns):
            try:
                if (matrix[i][j] != 0 ) and (matrix[i+1][j] != 0) and (matrix[i+1][j+1] != 0): # if blob is there
                    if (matrix[i-1][j-1] == 0 or IndexError) and (matrix[i-1][j] == 0 or IndexError) and (matrix[i-1][j+1] == 0 or IndexError): # Top part clear
                        if (matrix[i][j-1] == 0 or IndexError) and (matrix[i][j+1] == 0 or IndexError) and (matrix[i][j+2] == 0 or IndexError): # second lines clear
                            if (matrix[i+1][j-1] == 0 or IndexError) and (matrix[i+1][j+2] == 0 or IndexError): #third line clear
                                if (matrix[i+2][j-1] == 0 or IndexError) and (matrix[i+2][j] == 0 or IndexError) and (matrix[i+2][j+1] == 0 or IndexError) and (matrix[i+2][j+2] == 0 or IndexError): # last line clear
                                    matrix[i][j] = 0
                                    matrix[i+1][j] = 0
                                    matrix[i+1][j+1] = 0
            except IndexError:
                continue
 
 
    for i in matrix:
        print(*i)
#print(type_1(a))
 
def type_1(matrix):
    global count
    for i in range(rows):
        for j in range(columns):
            try:
                # if iszero( matrix,i,j) and iszero(matrix, I+1,j) and  iszero(matrix, i+1, j+1 )     ##   (matrix[i][j] != 0) and (matrix[i+1][j] != 0) and (matrix[i+1][j+1] != 0): # if blob is ther
                if (matrix[i][j] != 0) and (matrix[i+1][j] != 0) and (matrix[i+1][j+1] != 0): # if blob is there
                    #print(i,j)
                    if (matrix[i - 1][j - 1] == 0 or matrix[i - 1][j - 1] is IndexError) and (matrix[i - 1][j] == 0 or matrix[i - 1][j] is IndexError) and (matrix[i - 1][j + 1] == 0 or matrix[i - 1][j + 1] is IndexError):  # Top part clear
                        #print(i,j,'.')
                        if (matrix[i][j - 1] == 0 or matrix[i][j - 1] is IndexError) and (matrix[i][j + 1] == 0 or matrix[i][j + 1] is IndexError) and (matrix[i][j + 2] == 0 or matrix[i][j + 2] is IndexError):  # second lines clear
                            if (matrix[i + 1][j - 1] == 0 or matrix[i + 1][j - 1] is IndexError) and (matrix[i + 1][j + 2] == 0 or matrix[i + 1][j + 2] is IndexError):  # third line clear
                                if iszero1(matrix,i,j) is True:  # last line clear
                                    #print(matrix[i][j], matrix[i+1][j], matrix[i+1][j+1])
                                    matrix[i][j] = 0
                                    matrix[i + 1][j] = 0
                                    matrix[i + 1][j + 1] = 0
                                    count+=1
                                elif iszero1(matrix,i,j) is False:
                                    pass
                            else:
                                pass
                        else:
                            pass
                    else:
                        pass
                else:
                    pass
 
 
            except IndexError:
                continue
    for i in matrix:
        print(*i)
    print(count)
def iszero1(matrix,i,j):
    try:
        if (matrix[i + 2][j - 1] == 0 or matrix[i + 2][j - 1] is IndexError) and (matrix[i + 2][j] == 0 or matrix[i + 2][j] is IndexError) and (matrix[i + 2][j + 1] == 0 or matrix[i + 2][j + 1] is IndexError) and (matrix[i + 2][j + 2] == 0 or matrix[i + 2][j + 2] is IndexError):
            return True
        elif (matrix[i + 2][j - 1] != 0 or matrix[i + 2][j - 1] is not IndexError) or (matrix[i + 2][j] != 0 or matrix[i + 2][j] is not IndexError) or (matrix[i + 2][j + 1] != 0 or matrix[i + 2][j + 1] is not IndexError) or (matrix[i + 2][j + 2] != 0 or matrix[i + 2][j + 2] is not IndexError):
            return False
    except IndexError:
        return True
 
def iszero2(matrix,i,j):
    try:
        if (matrix[i + 1][j - 1] == 0 or matrix[i + 1][j - 1] is IndexError) and (matrix[i + 1][j] == 0 or matrix[i + 1][j] is IndexError) and (matrix[i + 1][j + 1] == 0 or matrix[i + 1][j + 1] is IndexError) and (matrix[i + 1][j + 2] == 0 or matrix[i + 1][j + 2] is IndexError):
            return True
        elif (matrix[i + 1][j - 1] != 0 or matrix[i + 1][j - 1] is not IndexError) or (matrix[i + 1][j] != 0 or matrix[i + 1][j] is not IndexError) or (matrix[i + 1][j + 1] != 0 or matrix[i + 1][j + 1] is not IndexError) or (matrix[i + 1][j + 2] != 0 or matrix[i + 1][j + 2] is not IndexError):
            return False
    except IndexError:
        return True
 
def type_3(matrix):
    for i in range(rows):
        for j in range(columns):
            try:
                # if iszero( matrix,i,j) and iszero(matrix, I+1,j) and  iszero(matrix, i+1, j+1 )     ##   (matrix[i][j] != 0) and (matrix[i+1][j] != 0) and (matrix[i+1][j+1] != 0): # if blob is ther
                if (matrix[i][j] != 0) and (matrix[i][j+1] != 0) and (matrix[i+1][j+1] != 0): # if blob is there
                    print("blob found")
                    if (matrix[i - 2][j] == 0 or IndexError) and (matrix[i - 2][j+1] == 0 or IndexError) and (matrix[i - 2][j + 2] == 0 or IndexError):  # Top part clear
                        if (matrix[i-1][j - 1] == 0 or IndexError) and (matrix[i-1][j] == 0 or IndexError) and (matrix[i-1][j + 2] == 0 or IndexError):  # second lines clear
                            if (matrix[i][j - 1] == 0 or IndexError) and (matrix[i][j + 2] == 0 or IndexError):  # third line clear
                                if iszero2(matrix,i,j) is True:  # last line clear
                                    #print("yayyy")
                                    #print(matrix[i][j], matrix[i+1][j], matrix[i+1][j+1])
                                    '''matrix[i][j] = 0
                                    matrix[i + 1][j] = 0
                                    matrix[i + 1][j + 1] = 0'''
                                elif iszero2(matrix,i,j) is False:
                                    pass
 
            except IndexError:
                continue
    for i in matrix:
        print(*i)
 
type_1(a)