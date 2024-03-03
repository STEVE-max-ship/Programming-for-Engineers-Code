import time

class Node:
    def __init__(self, key, depth, SR):
        self.left = None
        self.right = None
        self.key = key
        self.depth = depth
        self.SR = SR
        self.min_key = float('inf')

        self.sum_of_keys = 0

    def add_left(self, node):
        self.left = node

    def add_right(self, node):
        self.right = node

    def cost(self):
        return self.key * (self.depth + 1)

    def disbalance(self):
        SL, SR = 0, 0
        if self.left:
            SL = self.left.sum_of_keys
        if self.right:
            SR = self.right.sum_of_keys
        return abs(SL - SR)

    '''def sum_keys(self):
        res = self.key
        if self.left:
            res += self.left.sum_keys()
        if self.right:
            res += self.right.sum_keys()
        return res'''

    def is_leaf(self):
        return self.left is None and self.right is None




def build_node(key,depth, SR, AL, AR, C0, CL, CR, D, M):
    node = Node(key, depth, SR)
    if SR < C0 or depth == D:
        pass
    elif C0 <= SR < CL:
        node.add_left(build_node((AL*(key+1))%M, depth+1, (SR*AL)%M, AL, AR, C0, CL, CR, D, M))
    elif CL <= SR < CR:
        node.add_right(build_node((AR * (key + 2)) % M, depth + 1, (SR * AR) % M, AL, AR, C0, CL, CR, D, M))
    elif CR <= SR < M:
        left_node = build_node((AL*(key+1))%M, depth+1, (SR*AL)%M, AL, AR, C0, CL, CR, D, M)
        right_node = build_node((AR * (key + 2)) % M, depth + 1, (SR * AR) % M, AL, AR, C0, CL, CR, D, M)
        node.add_left(left_node)
        node.add_right(right_node)
    return node

#--------------------------------------------------------------------------------------------------------------

def sum_of_costs(node):
    if node is None:
        return 0
    return node.cost() + sum_of_costs(node.left) + sum_of_costs(node.right)

#----------------------------------------------------------------------------------------------------------------

def sum_of_disbalances(node):
    if node is None:
        return 0
    if node.left == None and node.right == None:
        node.sum_of_keys += node.key
        return node.disbalance()
    l = sum_of_disbalances(node.left)
    r = sum_of_disbalances(node.right)
    if node.left:
        node.sum_of_keys += node.left.sum_of_keys
    if node.right:
        node.sum_of_keys += node.right.sum_of_keys
    node.sum_of_keys += node.key
    return node.disbalance() + l + r

#----------------------------------------------------------------------------------------------------------------

'''def count_two_nodes(node):
    if node is None:
        return 0
    count = 0
    if node.left is not None and node.right is not None:
        count += 1
    count += count_two_nodes(node.left)
    count += count_two_nodes(node.right)
    return count

def two_balanced(node):
    if node is None:
        return 0
    if count_two_nodes(node.left) == count_two_nodes(node.right):
        total_sum = node.key
    else:
        total_sum = 0
    total_sum += two_balanced(node.left)
    total_sum += two_balanced(node.right)
    return total_sum'''


def count_two_nodes(node):
    if node is None:
        return 0

    if not hasattr(node, "count_cache"):
        node.count_cache = {}

    if node in node.count_cache:
        return node.count_cache[node]

    count = 0
    if node.left is not None and node.right is not None:
        count += 1
    count += count_two_nodes(node.left)
    count += count_two_nodes(node.right)

    node.count_cache[node] = count
    return count


def two_balanced(node):
    if node is None:
        return 0

    if not hasattr(node, "total_sum_cache"):
        node.total_sum_cache = {}

    if node in node.total_sum_cache:
        return node.total_sum_cache[node]

    if count_two_nodes(node.left) == count_two_nodes(node.right):
        total_sum = node.key
    else:
        total_sum = 0
    total_sum += two_balanced(node.left)
    total_sum += two_balanced(node.right)

    node.total_sum_cache[node] = total_sum
    return total_sum


# 1.30 seconds (gives right output)
# 0.4 seconds (gives right output)
#---------------------------------------------------------------------------------------------------------

def parity_siblings(node):
    def counter(node):
        if not node:
            return 0, 0
        left_n, left_p = counter(node.left)
        right_n, right_p = counter(node.right)
        total_n = left_n + right_n
        if node.left and node.right and (node.left.key % 2) == (node.right.key % 2):
            total_n += 1
        return total_n, node.key % 2
    return counter(node)[0]

#---------------------------------------------------------------------------------------------------------

'''def min_key(node):
    if node is None:
        return float('inf')
    elif node.is_leaf():
        return node.key
    else:
        return min(node.key, min_key(node.left), min_key(node.right))

def sum_of_minimals(node):
    if node is None:
        return 0
    sum_of_keys = 0
    if node.is_leaf() or node.key <= min_key(node):
        sum_of_keys += node.key
    sum_of_keys += sum_of_minimals(node.left)
    sum_of_keys += sum_of_minimals(node.right)
    return sum_of_keys'''


def min_key(node):
    if node is None:
        return float('inf')
    elif node.left is None and node.right is None:
        return node.key

    if node.min_key != float('inf'):
        return node.min_key

    node.min_key = min(node.key, min_key(node.left), min_key(node.right))
    return node.min_key


def sum_of_minimals(node):
    if node is None:
        return 0

    sum_of_keys = 0
    if node.left is None and node.right is None or node.key <= min_key(node):
        sum_of_keys += node.key

    sum_of_keys += sum_of_minimals(node.left)
    sum_of_keys += sum_of_minimals(node.right)

    return sum_of_keys
# 1.03 seconds (gives right output)
# 0.13 seconds (gives right output)
#---------------------------------------------------------------------------------------------------------------

'''def count_weakly_dominant_nodes(node):
    if node is None:
        return
    count = 0
    stack = [node]
    while stack:
        var = stack.pop()
        if var is None:
            continue
        if (var.left or var.right) and var.key >= max_leaf(var):
            count += 1
        stack.append(var.left)
        stack.append(var.right)
    return count


def max_leaf(node):
    if node is None:
        return
    stack = [node]
    max_leaf = node.key
    while stack:
        var = stack.pop()
        if var is None:
            continue
        if var.left is None and var.right is None:
            max_leaf = max(max_leaf, var.key)
        stack.append(var.left)
        stack.append(var.right)
    return max_leaf'''


def max_leaf(node):
    if node is None:
        return None

    if node.left is None and node.right is None:
        return node.key

    max_left = max_leaf(node.left) if node.left else float('-inf')
    max_right = max_leaf(node.right) if node.right else float('-inf')

    return max(max_left, max_right)


def count_weakly_dominant_nodes(node):
    if node is None:
        return 0

    count = 0

    if node.left is None and node.right is None:
        node.max_leaf = node.key
        return 0

    left_count = count_weakly_dominant_nodes(node.left)
    right_count = count_weakly_dominant_nodes(node.right)

    if node.left is None:
        if node.key >= node.right.max_leaf:
            node.max_leaf = node.right.max_leaf
            count += 1
        else:
            node.max_leaf = node.right.max_leaf
    elif node.right is None:
        if node.key >= node.left.max_leaf:
            node.max_leaf = node.left.max_leaf
            count += 1
        else:
            node.max_leaf = node.left.max_leaf
    else:
        if node.key >= node.left.max_leaf and node.key >= node.right.max_leaf:
            if node.left.max_leaf >= node.right.max_leaf:
                node.max_leaf = node.left.max_leaf
            else:
                node.max_leaf = node.right.max_leaf
            count += 1
        else:
            if node.left.max_leaf >= node.right.max_leaf:
                node.max_leaf = node.left.max_leaf
            else:
                node.max_leaf = node.right.max_leaf

    return count + left_count + right_count


# 1.18 seconds (gives right output)
# 0.05 seconds (gives right output)
#-----------------------------------------------------------------------------------------------

def left_only(node):
    if node is None:
        return False
    elif node.left and not node.right:
        return True
    return left_only(node.left) or left_only(node.right)

def right_only(node):
    if node is None:
        return False
    elif node.right and not node.left:
        return True
    return right_only(node.left) or right_only(node.right)

def right_and_left_l1(node):
    return left_only(node) and not right_only(node)


def total_l1(node):
    if node is None: 
        return 0 
    curr = 0 
    if right_and_left_l1(node):
        curr = 1 
    return curr + total_l1(node.left) + total_l1(node.right)


# 0.7 seconds (gives right output)
#----------------------------------------------------------------------------------------------------

def build_max_increasing_path(node):
    if node is None:
        return 0
    left_path = 0
    if node.left and node.left.key >= node.key:
        left_path = build_max_increasing_path(node.left)
    right_path = 0
    if node.right and node.right.key >= node.key:
        right_path = build_max_increasing_path(node.right)
    return max(left_path, right_path) + node.key


def max_increasing_path(node):
    if node is None:
        return 0
    path_through_root = build_max_increasing_path(node)
    left_path = max_increasing_path(node.left)
    right_path = max_increasing_path(node.right)
    return max(path_through_root, left_path, right_path)





input_str = input().strip()  # read input as string
AL, AR, C0, CL, CR, D, M, RK, RSR = map(int, input_str.split())
key = RK
root = build_node(key, 0, RSR, AL, AR, C0, CL, CR, D, M)
t1 = time.time()
cost = sum_of_costs(root)
t2 = time.time()
#print("cost:", t2-t1)
disbalance = sum_of_disbalances(root)
t3 = time.time()
#print("disbalance:", t3-t2)
two_bal = two_balanced(root)
t4 = time.time()
#print("2bal:", t4-t3)
parity = parity_siblings(root)
t5 = time.time()
#print("parity:", t5-t4)
locally_minimal = sum_of_minimals(root)
t6 = time.time()
#print("locally minimal:", t6 - t5)
weakly_dominant = count_weakly_dominant_nodes(root)
t7 = time.time()
#print("weakly dominant:", t7-t6)
L1_trees = total_l1(root)
t8 = time.time()
#print("L1 trees:", t8-t7)
increasing_path = max_increasing_path(root)
t9 = time.time()
#print("increasing path:", t9 - t8)
print(cost)
print(disbalance)
print(two_bal)
print(parity)
print(locally_minimal)
print(weakly_dominant)
print(L1_trees)
print(increasing_path)
#print("overall time:", t9 - t1)









