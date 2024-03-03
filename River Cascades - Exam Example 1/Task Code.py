R,C,L = input().split()
R,C,L = int(R),int(C),int(L)
a = []
#b = []
new = []
style = []
for i in range(R):
    rows = input().split()
    a.append(rows)
for i in a:
    for j in range(len(i)):
        i[j] = int(i[j])

b = [[a[i][j] for i in range(len(a))] for j in range(len(a[0]))]





def nfinder(lst, n):
    new = []
    inside_new = []
    count = 0
    baby_counter = 0
    try:
        for i in range(len(lst)):
            if lst[i] == 0:
                continue
            if lst[i] != 0:
                for j in range(n):
                    if lst[i+j] != 0:
                        count+=1
                    else:
                        count = 0
                if count == n:
                    for z in range(n):
                        inside_new.append(lst[i+z])
                    count = 0
                    new.append(inside_new)
                    inside_new = []
                else:
                    count = 0
    except IndexError:
        return new
        pass
    testing = []
    '''for i in new:
        for j in i:
            testing.append(j)
    for i in testing:
        if testing.count(i) == 2:
            baby_counter +=1
    if baby_counter >= 2:
        del new[-1]
    return new'''

def n_cascades(lst,n):
    counter = 0
    new = []
    def happy_cascade(lst):
        for baby in lst:
            if baby[1] != baby[0] - 1 and baby[len(baby) - 2] != baby[-1] + 1:
                return True
            else:
                return False
    def is_ordered(lst, n):
        count = 0
        try:
            for i in range(len(lst)):
                if lst[i] == lst[i + 1] - 1:
                    count += 1
        except IndexError:
            if count == n - 1:
                return True
            else:
                return False
    for i in lst:
        if is_ordered(i,n) is True:
            new.append(i)

    if happy_cascade(new) is True:
        counter +=1
    else:
        pass
    return counter

def exam_saver(matrix,L):
    final = []
    for i in matrix:
        mylist = nfinder(i,L)
        if mylist == [] or mylist is None:
            continue
        else:
            final.append(n_cascades(mylist,L))
    print(sum(final))
        #print(mylist)




#print(b)
exam_saver(a,L)
exam_saver(b,L)

