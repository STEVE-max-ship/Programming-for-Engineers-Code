R,C,NQ = input().split()
R,C,NQ = int(R),int(C),int(NQ)
a = []
queries = []
for i in range(R):
    rows = input().split()
    a.append(rows)
for i in range(R):
    for j in range(C):
        a[i][j] = int(a[i][j])
for i in range(NQ):
    qs = input().split()
    queries.append(qs)
for i in range(NQ):
    for j in range(4):
        queries[i][j] = int(queries[i][j])


def rectangle_finder(matrix, one_query):
    submatrix = []
    helper = []
    verticle_helper = []
    R1 = one_query[0]
    C1 = one_query[1]
    R2 = one_query[2]
    C2 = one_query[3]
    ncolumns = abs(C2 - C1) + 1
    nrows = abs(R2 - R1) + 1
    for i in range(nrows):
        for j in range(ncolumns):
            helper.append(matrix[R1 + i][C1 + j])
        submatrix.append(helper)
        helper = []

    for i in submatrix:
        if len(i) == 1:
            verticle_helper.append(i[0])
            submatrix = []
    if len(verticle_helper) != 0:
        submatrix = [verticle_helper]

    return submatrix

def happy_rectangle(submatrix):
    try:
        V1 = submatrix[0][0]
        V2 = submatrix[0][1]
    except IndexError:
        pass
    for i in submatrix:
        for j in i:
            if j != V1 and j != V2:
                return False

    for i in range(len(submatrix)):
        for j in range(len(submatrix[0])):
            try:
                if submatrix[i][j] == submatrix[i][j+1]:
                    return False
            except IndexError:
                pass

    transposed_submatrix = [[submatrix[j][i] for j in range(len(submatrix))] for i in range(len(submatrix[0]))]

    for i in range(len(transposed_submatrix)):
        for j in range(len(transposed_submatrix[0])):
            try:
                if transposed_submatrix[i][j] == transposed_submatrix[i][j+1]:
                    return False
            except IndexError:
                pass
    return True

def main_worker(matrix):
    for i in queries:
        #print(rectangle_finder(matrix,i))
        if happy_rectangle(rectangle_finder(matrix,i)) is True:
            print(*i,"True")
        if happy_rectangle(rectangle_finder(matrix,i)) is False:
            print(*i,"False")

main_worker(a)
