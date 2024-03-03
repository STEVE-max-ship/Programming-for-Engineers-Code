

def task01( matrix ):
    col = zip(*matrix)
    new_list = []
    result = []
    for rows in col:
        lst = []
        for i in rows:
            if i not in lst:
                lst.append(i)
            else:
                pass
        if len(lst) == 2:
            new_list.append(rows)
        else:
            new_list.append("None")


    for x in new_list:
        if x != "None":
            result.append(new_list.index(x))

    print(*result)

def task02( matrix ):
    max_vals = []
    for i in range(len(matrix) - 1):
        for x in range(len(matrix[i]) - 1):
            temp = matrix[i][x] + matrix[i][x+1] + matrix[i+1][x] + matrix[i+1][x+1]
            max_vals.append(temp)
    max_num = max(max_vals)
    max_count = max_vals.count(max_num)

    print(max_num,max_count)

def task03(matrix):
    P = []
    rows20 = []
    matrix20 = []
    a = len(matrix) - 1
    sumzero = []
    for lists in reversed(matrix):
        for i in range(len(lists)):
            if lists[i] == 0:
                lists[i] = sum(lists[i+1:]) + sum(matrix[j][i] for j in range(a))
                sumzero.append(sum(lists[i+1:]) + sum(matrix[j][i] for j in range(a)))
        a -= 1
    if len(matrix) > 20:
        for i in matrix:
            row = i[-20:]
            rows20.append(row)
        matrix20 = rows20[-20:]
        P = matrix20
        for mylists in P:
            print(*mylists, end=" ")
            print()
    if len(matrix) < 20:
        P = matrix
        for mylists in P:
            print(*mylists, end=" ")
            print()
    print(sum(sumzero))




















# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
#               I N P U T    R E A D I N G
taskNo = int(input())
R, C = map(int, input().split())
arr2d = []
for i in range(R):
    row = list(map(int, input().split()))
    arr2d.append(row)

# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
#             P R O C E S S I N G


if taskNo == 1:  task01(arr2d)
if taskNo == 2:  task02(arr2d)
if taskNo == 3:  task03(arr2d)
if taskNo == 4:  task04(arr2d)
if taskNo == 5:  task05(arr2d)