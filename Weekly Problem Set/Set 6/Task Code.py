import time
import math
def task01(N, K):
    result = math.comb(N, K)
    print(result)

def task02(N, K):
    count = 0
    def count_strings(n, k, prev_char):
        nonlocal count
        if n == 0 and k == 0:
            count += 1
            return
        if n > 0:
            count_strings(n - 1, k, tiny)
        if k > 0 and prev_char != huge:
            count_strings(n - 1, k - 1, huge)
    tiny = 'o'
    huge = 'I'
    count_strings(N, K, tiny)
    print(count)

def task03(lst):
    def generate_tuples(sub_list, current_tuple, demanded_sum, result):
        if not sub_list:
            if sum(current_tuple) == demanded_sum and current_tuple:
                result.append(tuple(current_tuple))
            return

        generate_tuples(sub_list[1:], current_tuple + [sub_list[0]], demanded_sum, result)
        generate_tuples(sub_list[1:], current_tuple, demanded_sum, result)

    non_zero_list = [num for num in lst if num != 0]
    tuples = []
    generate_tuples(non_zero_list, [], 0, tuples)
    unique_tuples = list(set(tuples))
    print(len(unique_tuples))








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
for aList in inputLists:
    if taskNo == 1:  task01( aList[0], aList[1] )
    if taskNo == 2:  task02( aList[0], aList[1] )
    if taskNo == 3:  task03( aList )
    if taskNo == 4:  task04( aList ) # number of oranges and paket prices
    if taskNo == 5:  task05( aList )

t2 = time.time()
# print( 'time', str(t2-t1)[:5] )