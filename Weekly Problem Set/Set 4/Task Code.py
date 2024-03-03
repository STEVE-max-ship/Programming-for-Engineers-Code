import time,functools

def task01(lists):
    minindex = []
    maxindex = []
    for i in range(1, len(lists)-1):
        if lists[i] < lists[i+1] and lists[i] < lists[i-1]:
            minindex.append(i)
    '''for i in range(0, len(lists)):
        if lists.count(max(lists)) > 1:
            if i is lists.index(max(lists)):
                maxindex.append(i)
                lists[i] = 0'''
    for i in range(0, len(lists)):
        if lists[i] is max(lists):
            maxindex.append(i)
        else:
            if i is lists.index(max(lists)):
                maxindex.append(i)
    final = []
    for i in minindex:
        result = []
        for x in maxindex:
            result.append(abs(i-x))
        final.append(min(result))
    if len(final) == 0:
        print(0)
    else:
        print(sum(final))

def task02(lists):
    minindex = []
    maxindex = []
    depth = []
    value = []
    m = ()
    for i in range(1, len(lists) - 1):
        if lists[i] < lists[i + 1] and lists[i] < lists[i - 1]:
            minindex.append(i)
            value.append(lists[i])
            if lists[i-1] - lists[i] < lists[i+1] - lists[i]:
                depth.append(lists[i-1] - lists[i])
            else:
                depth.append(lists[i+1] - lists[i])
    for i in range(0, len(lists)):
        if lists[i] is max(lists):
            maxindex.append(i)
        else:
            if i is lists.index(max(lists)):
                maxindex.append(i)
    final = []
    for i in minindex:
        result = []
        for x in maxindex:
            result.append(abs(i - x))
        final.append(min(result))

    for x in minindex:
        for y in depth:
            for z in final:
                for j in value:
                    m = (x,y,z,j)
    #print(minindex)
    #print(depth)
    #print(final)
    #print(value)
    #print(m)
    result = []
    for temp in zip(minindex, depth, final, value):
        result.append(temp)
    #print(result)
    result = sorted(result, key=functools.cmp_to_key(compCOMP))
    for i in result:
        print(*i)
    print()


def compCOMP(a, b):
    if a[1] > b[1]:
        return 1
    elif a[1] < b[1]:
        return -1

    elif a[2] > b[2]:
        return 2
    elif a[2] < b[2]:
        return -2

    elif a[3] < b[3]:
        return -3
    elif a[3] > b[3]:
        return 3
    return 3

'''def task03(lists): # sliding window could be used
    a = 1
    goal = sum(lists)/2
    for i in range(0,a):
        if lists[i] + lists[i+1] < goal:
            pass
        elif lists[i] + lists[i+1] >= goal:
            print("yay")
        a += 1
    print(goal)'''

'''def task03(lists):
    goal = sum(lists)/2
    #a = 0
    #b = 1

    for i in range(len(lists)):
        a = 0
        b = 1
        try:
            for j in range(a,b):
                if lists[i] + lists[i+1] < goal:
                    a+=1
                    b+=1
                elif lists[i] + lists[i+1] >= goal:
                    print(i,i+1,lists[i] + lists[i+1])
                    #pass

            a = 0
            b = 1
        except IndexError:
            print("broken")


    #print(goal)'''
'''def task03(lists):
    goal = sum(lists)/2
    current = []
    m = ()
    start = 0
    end = 0
    for i in range(len(lists)):
        if sum(current) < goal:
            current.append(lists[i])
            start = i

        elif sum(current) >= goal:
            m = (0,i-1,sum(current))
            current.pop(0)'''

def task03(lists):
    goal = sum(lists)/2
    minlength = 0
    new = []
    sub = []
    all = []
    result = []
    total = []
    for i in range(len(lists)):
        if sum(sub) < goal:
            sub.append(lists[i])
            new.append(i)
        while sum(sub) >= goal:
            all.append(list(new))
            sub.pop(0)
            new.pop(0)
            minlength = len(sub)
    #print(new)
    #print(sub)

    for i in (min(all,key=len)):
        result.append(i)
        if len(result) > 2:
            result.pop(1)
    for j in (min(all,key=len)):
        if len(result) == 1:
            result.extend(result)
            total.append(lists[j])
            #total.pop(0)
        elif len(result) > 1:
            total.append(lists[j])
    print(*result, sum(total))
    #print(min(all, key=len))
    #print(all)
    #print(lists)
    #print()

    #print(total)

























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
if taskNo == 5:
    for i in range(0, len(inputLists), 2):  # targets and shots
        task05(inputLists[i], inputLists[i + 1])

t2 = time.time()
# print( 'time', str(t2-t1)[:5] )