from typing import List
from random import randint
class p_Gen:
    def __init__(self):
        self.cnt = 0
        self.prt = set()
    def gen(self):
        p = randint(0, 2**20)
        while (p in self.prt):
            p = ranint(0, 2**20)
        self.prt.add(p)
        return p

class Node:
    def __init__(self, prioriety, val, rank, s, par=None):
        self.prioriety = prioriety
        self.val = val
        self.rank = rank
        self.sum = s
        self.right = None
        self.left = None
        self.par = par

    def __str__(self):
        return f'p: {self.prioriety}, v: {self.val}, rank: {self.rank}, s: {self.sum} '
    
def merge(node1, node2):
    if not node1: return node2
    if not node2: return node1
    if node1.prioriety < node2.prioriety:
        node1.right = merge(node1.right, node2)
        update(node1)
        return node1
    else:
        node2.left = merge(node1, node2.left)
        update(node2)
        return node2

def splitBySize(node, k):
    if not node: return (None, None)
    l = 0 if not node.left else node.left.rank
    if k <= l:
        ll, lr = splitBySize(node.left, k)
        node.left = lr
        update(node)
        return ll, node
    else:
        rl, rr = splitBySize(node.right, k - l - 1)
        node.right = rl
        update(node)
        return node, rr

def insert(treap, val, pos, gen):
    r, l = splitBySize(treap, pos - 1)
    node = Node(gen.gen(), val, 1, val)
    r = merge(r, node)
    r = merge(r, l)
    return r

def erase(root, pos):
    l,r = splitBySize(root, pos -1 )
    rl, rr = splitBySize(r, 1)
    merge(l, rr)

def sum(root, frm, to):
    l,r = splitBySize(root, frm -1 )
    rl, rr = splitBySize(r, to - frm + 1)
    return rl.sum

def make(a, g):
    n = len(a)
    nodes = [Node(g.gen(), a[i], 1, a[i]) for i in range(n)]
    root = nodes[0]
    for i in range(1, n):
        root = merge(root, nodes[i])
    return root

def printTreap(root):
    def printTreapAsArr(root):
        if not root : return
        printTreapAsArr(root.left)
        print(root.val, end = ' ')
        printTreapAsArr(root.right)
    printTreapAsArr(root)
    print()

def update(root):
    rank_left = 0 if not root.left else root.left.rank
    sum_left = 0 if not root.left else root.left.sum
    rank_right = 0 if not root.right else root.right.rank
    sum_right = 0 if not root.right else root.right.sum
    root.rank = 1 + rank_left + rank_right
    root.sum = sum_left + sum_right + root.val

def serialize(root):
    def dfs(root, arr):
        if not root:
            arr.append('x')
            return
        arr.append('(')
        arr.append(f'[{root.val}, {root.rank}, {root.sum}]')
        dfs(root.left, arr)
        dfs(root.right, arr)
        arr.append(')')
    arr = []
    dfs(root, arr)
    return(' '.join(arr))

gen = p_Gen()
l = [1,2,3,4,5]
pos = 3
root = make(l, gen)
print(sum(root, 2, 4))
