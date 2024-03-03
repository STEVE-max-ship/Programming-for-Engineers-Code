def task01(List1, List2):
    print(len([x for x in List1 if x < List1[0]]))
    print(len([x for x in List2 if x < List2[0]]))


def task02(List1):
    ld_count = 0
    tr_count = 0
    for i in List1:
        if i == 0:
            ld_count += 1
        else:
            break
    List1.reverse()
    for i in List1:
        if i == 0:
            tr_count += 1
        else:
            break

    if ld_count == tr_count:
        print("True")
    else:
        print("False")


def task03(List1, List2):
    min1 = min(List1)
    max2 = max(List2)
    for i in range(len(List2)):
        if List2[i] == max2:
            List2[i] = min1

    print(*List2)


def task04(List1):
    new_list1 = []
    for i in List1:
        if List1.count(i) == 2:
            new_list1.append(i)
    if new_list1 == []:
        print("None")
    else:
        print(min(new_list1))

def task05(matrix):
    matrix.pop(0)
    matrix.pop(-1)
    for i in matrix:
        i.pop(0)
        i.pop(-1)
    for mylists in matrix:
        print(*mylists, end=" ")
        print()

def task06(matrix):
    var = 0
    var2 = -1
    for lists in matrix:
        lists[var], lists [var2] = lists[var2], lists[var]
        var += 1
        var2 -= 1
        print(*lists)


# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
#               I N P U T    R E A D I N G
taskNo = int(input())
if taskNo in [1, 2, 3, 4]:
    list1 = list(map(int, input().split()))
    list2 = list(map(int, input().split()))
if taskNo in [5, 6]:
    matrixSize = int(input())
    matrix = []
    for i in range(matrixSize):
        row = list(map(int, input().split()))
        matrix.append(row)

# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
#             P R O C E S S I N G

if taskNo == 1:
    task01(list1, list2)

if taskNo == 2:
    task02(list1)
    task02(list2)

if taskNo == 3:
    task03(list1, list2)

if taskNo == 4:
    task04(list1)
    task04(list2)

if taskNo == 5:
    task05(matrix)

if taskNo == 6:
    task06(matrix)



