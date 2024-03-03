rows,columns = input().split()
rows,columns = int(rows),int(columns)
a = []
b = []
for i in range(rows):
    helper = input().split()
    a.append(helper)
for i in range(rows):
    for j in range(columns):
        a[i][j] = int(a[i][j])
isok = True
tester = True
result = []
for i in range(1):
    i = 3
    b = []
    b = a.copy()
    if b[i].count(1) >= 2:
        new = []
        for j in range(columns):# gets poles coordinates
            if b[i][j] == 1:
                new.append([i,j])
        for z in range(len(new)-1):# iterates over first set of poles, then next
            pole1 = new[z]
            pole2 = new[z+1]
            thick = abs(pole2[1]-pole1[1]-1)
            for net in range(thick):
                b[pole1[0]][pole1[1]+net+1] = "x"
                '''for top in range(rows-1):
                    if (pole1[0]-(top+1)) >= 0:
                        if b[pole1[0]-(top+1)][pole1[1]+net+1] == 0:
                            b[pole1[0] - (top+1)][pole1[1] + net + 1] = "x"
                        elif b[pole1[0]-(top+1)][pole1[1]+net+1] == 1:
                            for last in range(thick):
                                b[pole1[0]-(top+1)][pole1[1]+last+1] = "n"
                            break
                    elif (pole1[0]-(top+1)) < 0:
                        break'''

                try:
                        for bottom in range(rows-1):
                            if isok is True:
                                for side in range(thick):
                                    if b[pole1[0]+(bottom+1)][pole1[1]+side+1] == 0:
                                        b[pole1[0] + (bottom + 1)][pole1[1] + side + 1] = "x"
                                    elif b[pole1[0]+(bottom+1)][pole1[1]+side+1] == 1:
                                        for last in range(thick):
                                            b[pole1[0] + (bottom + 1)][pole1[1] + last + 1] = "n"
                                        isok = False
                            elif isok is False:
                                break
                except IndexError:
                    break

        for h in b:
            print(*h)

        print(new)


#print(b)

