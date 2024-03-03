import time
def task01(strings):
    A = []
    B = []
    c = 0
    for i in strings:
        string_len = len(strings[c])
        if string_len % 2 == 0:
            A.append(i[0:string_len//2])
            B.append(i[string_len//2:])

        else:
            string_len = int((string_len/2) + 0.5)
            A.append(i[0:string_len])
            B.append(i[string_len:])

        c+=1
    print("".join(A))
    print("".join(B))

def task02(string:list):
    result=[]
    for i in string:
        temp = []
        for x in range(0,len(i)):
            for y in range(x+1, len(i)+1):
                if i[x:y].count("1") == 1 and i[x:y].count("0") == 1 and i[x:y] not in result:
                    temp.append(i[x:y])
                else:
                    pass
        print(len(temp))

'''def task03(strings):
    last_char = ""
    for i in strings:
        for char in i:
            if last_char == char:
                i = list(i)
                
                ind = i.index(char)
                ind2 = i.index(last_char)
                del i[ind]
                del i[ind2]
                i = str(i)
                #i = i.replace(char, "")
                #i = i.replace(last_char, "")
            else:
                pass
            last_char = char

        print(i)'''

def task03(strings):
    temp = strings[:]
    #prev = ""
    for _ in range(5):
        #prev = ""
        for a, i in enumerate(temp):
            prev = ""
            word = list(i)
            for i in range(len(word)):
                if word[i] == prev:
                    prev = word[i]
                    word[i] = ""
                    word[i - 1] = ""
                else:
                    prev = word[i]
            if len(set(word)) == 1:
                #print("None", end="")
                pass
            temp[a] = "".join(word)
    #print(temp)
    for b in temp:
        if b == "":
            print("None")
        else:
            print(b)
            #print(word)

'''def task03(strings):
    while True:
        new_strings = []
        for word in strings:
            new_word = [word[0]]
            for i in range(1, len(word)):
                if word[i] != new_word[-1]:
                    new_word.append(word[i])
            new_strings.append(''.join(new_word))
        if new_strings == strings:
            break
        strings = new_strings

    for word in strings:
        if len(set(word)) == 1:
            print("None")
        else:
            print(word)'''

def task04(string):

















# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
#               I N P U T    R E A D I N G
taskNo = int(input())
Nstrings = int(input())
strings = []
for k in range(Nstrings):
    strings.append(input())

# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
#             P R O C E S S I N G

t1 = time.time()
if taskNo == 1:  task01(strings)
if taskNo == 2:  task02(strings)
if taskNo == 3:  task03(strings)
if taskNo == 4:  task04(strings)
if taskNo == 5:  task05(strings)
t2 = time.time()
# print( 'time', str(t2-t1)[:5] )