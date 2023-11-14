from typing import List
from random import shuffle

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

def makeTreap(a) -> Node:
    n = len(a)
    priorities = [i for i in range(n)]
    shuffle(priorities)
    nodes = [Node(priorities[i], a[i], 1, a[i]) for i in range(n)]
    root = nodes[0]
    for i in range(1, n):
        prev = nodes[i-1]
        curr = nodes[i]
        if prev.prioriety < curr.prioriety:
            prev.right = curr
            curr.par = prev
        else:
            while(prev.par and prev.par.prioriety > curr.prioriety):
                prev = prev.par
            if prev.par == None:
                root = curr
                prev.par = curr
            else:
                prev.par.right = curr
                prev.par, curr.par = curr, prev.par
            curr.left = prev
    return root

def printTreapAsArr(root):
    if not root : return
    printTreapAsArr(root.left)
    print(root.val, end = ' ')
    printTreapAsArr(root.right)


def update(root):
    rank_left = 0 if not root.left else root.left.rank
    sum_left = 0 if not root.left else root.left.sum
    rank_right = 0 if not root.right else root.right.rank
    sum_right = 0 if not root.right else root.right.sum
    root.rank = 1 + rank_left + rank_right
def serialize(root):
    def dfs(root, arr):
        if not root:
            arr.append('x')
            return
        arr.append('(')
        arr.append(f'[{root.val}, {root.prioriety}]')
        dfs(root.left, arr)
        dfs(root.right, arr)
        arr.append(')')
    arr = []
    dfs(root, arr)
    return(' '.join(arr))

l = [1, 2, 3, 4, 5]
root = makeTreap(l)
print(serialize(root))