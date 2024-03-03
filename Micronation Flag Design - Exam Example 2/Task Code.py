rows, columns, leftpart_columns, leftpart_stripe_width, rightpart_stripe_width, C1, C2 = input().split()
rows, columns, leftpart_columns, leftpart_stripe_width, rightpart_stripe_width, C1, C2 = int(rows), int(columns), int(leftpart_columns), int(leftpart_stripe_width), int(rightpart_stripe_width), int(C1), int(C2)
a = []
for i in range(rows):
    new = []
    for j in range(columns):
        new.append(0)
    a.append(new)
rightpart_columns = columns - leftpart_columns

leftcounter = 0
leftadder = 0
for i in range(int(leftpart_columns/leftpart_stripe_width)):
    if leftcounter == 0:
        for j in range(leftadder, leftpart_stripe_width+leftadder):
            for g in range(rows):
                a[g][j] = C1
        leftcounter += 1
    elif leftcounter == 1:
        for j in range(leftadder, leftpart_stripe_width+leftadder):
            for g in range(rows):
                a[g][j] = C2
        leftcounter -= 1
    leftadder+=leftpart_stripe_width

rightcounter = 0
rightadder = 0
for i in range(int(rows/rightpart_stripe_width)):
    if rightcounter == 0:
        for j in range(rightpart_columns):
            for g in range(rightadder, rightpart_stripe_width+rightadder):
                a[g][j+leftpart_columns] = C1
        rightcounter+=1
    elif rightcounter == 1:
        for j in range(rightpart_columns):
            for g in range(rightadder, rightpart_stripe_width+rightadder):
                a[g][j+leftpart_columns] = C2
        rightcounter-=1
    rightadder+=rightpart_stripe_width
for i in a:
    print(*i,sep='')
