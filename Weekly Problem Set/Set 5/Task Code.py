import time
import random

'''def task01(arr):
    r = 0
    cell1 = 0
    cnt = []
    for i in arr:
        if i != 0:
            cell1+=1

    for i in range(1):
        r = arr[cell1-1] # num in 4 is r
        arr[cell1*r] = r # num in 5 or 10 becomes r
        arr[cell1-1] = 0 # num in 4 becomes 0
        cnt.append(cell1)
        #cnt.append((cell1 - 1) / 2)
        a = 2
        one = 0
        two = 0
        if r == 1:
            one = 1
        elif r == 2:
            two = 1
        for j in range(cell1-1):
            cnt.append(abs(cell1*r-(cell1-a))) # appends backwards from 5 or 10 to 3
            r = arr[cell1-a] # num in 3 is r
            arr[cell1-a] = 0 # num in 3 becomes 0

            if r == 1:
                arr[cell1*r+one] = r # num in 6 becomes 1
                cnt.append(abs((cell1*r+one)-(cell1-a)))
                r = arr[cell1*r+one]
                one+=1
            elif r == 2:
                arr[cell1*r+two] = r # num in 10 becomes 1
                cnt.append(abs((cell1*r+two)-(cell1-a)))
                r = arr[cell1*r+two]
                two+=1

            a+=1

    #print(arr)
    #print(cell1)
    print(sum(cnt))'''
def task01(arr):
    r = 0
    cell1 = 0
    cnt = []
    for i in arr:
        if i != 0:
            cell1 += 1

    r = arr[cell1 - 1]  # num in 4 is r
    arr[cell1 * r] = r  # num in 5 or 10 becomes r
    arr[cell1 - 1] = 0  # num in 4 becomes 0
    cnt.append(cell1 * r)
    # cnt.append((cell1 - 1) / 2)
    a = 2
    temp = cell1 * r
    one = 0
    two = 0
    if r == 1:
        one = 1
    elif r == 2:
        two = 1
    for j in range(cell1 - 1):
        cnt.append(abs(temp - (cell1 - a)))  # appends backwards from 5 or 10 to 3
        r = arr[cell1 - a]  # num in 3 is r
        arr[cell1 - a] = 0  # num in 3 becomes 0

        if r == 1:
            arr[cell1 * r + one] = r  # num in 6 becomes 1
            cnt.append(abs((cell1 * r + one) - (cell1 - a)))
            r = arr[cell1 * r + one]
            temp = cell1 * r + one
            one += 1
        elif r == 2:
            arr[cell1 * r + two] = r  # num in 10 becomes 1
            cnt.append(abs((cell1 * r + two) - (cell1 - a)))
            r = arr[cell1 * r + two]
            temp = cell1 * r + two
            two += 1

        a += 1
    #print(cnt)

    print(sum(cnt))

def task02(arr):
    r = 0
    a = 0
    cell1 = arr[:len(arr)//2]
    lencell1 = len(cell1)
    cnt = []
    cnt.append(lencell1)
    cell1[cell1.index(min(cell1))] = 20001
    for i in range(lencell1-1):
        c = cell1.index(min(cell1))
        cnt.append(abs((lencell1+a)-(c)))
        a+=1
        cnt.append(abs((lencell1+a)-(c)))
        cell1[c] = 20001
    print(sum(cnt))

'''def task02(arr):
    cell1 = arr[:len(arr) // 2]
    moded = sorted(cell1)
    lencell1 = len(cell1)
    cnt = 0
    a = 0
    count = 0
    for i in moded:
        if count == 0:
            cnt = cnt+(lencell1)
        else:
            c = cell1.index(i)
            cnt = cnt + abs((lencell1 + a) - (c))
            a += 1
            cnt = cnt + abs((lencell1 + a) - (c))

        count+=1
    print(cnt)'''

def task04(arr):
    diction = {}
    sign = []
    for idx, item in enumerate(arr):
        if item not in diction:
            diction[item] = []
        diction[item].append(idx)

    for idx, item in enumerate(arr):
        half = item // 2
        double = item * 2

        left = 0
        right = 0
        if half in diction and double not in diction:
            for i in diction[half]:
                if i < idx:
                    left += 1
        elif double in diction and half not in diction:
            for i in diction[double]:
                if i > idx:
                    right += 1
        if half in diction and double in diction:
            for i in diction[half]:
                if i < idx:
                    left += 1
            for i in diction[double]:
                if i > idx:
                    right += 1
        sign.append(left + right)

    print(*sign)





















# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
#               I N P U T    R E A D I N G
taskNo = int(input())
Nlists = int(input())
inputLists = []
for k in range(Nlists):
    oneList = list(map(int, input().split()))
    inputLists.append(oneList)

# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
#             P R O C E S S I N G

t1 = time.time()
if taskNo in [1, 2, 3, 4]:
    for aList in inputLists:
        if taskNo == 1:  task01(aList)
        if taskNo == 2:  task02(aList)
        if taskNo == 3:  task03(aList)
        if taskNo == 4:  task04(aList)
if taskNo in [5]:
    for i in range(0, len(inputLists), 2):  # pairs of lists
        task05(inputLists[i], inputLists[i + 1])

t2 = time.time()
# print( 'time', str(t2-t1)[:5] )