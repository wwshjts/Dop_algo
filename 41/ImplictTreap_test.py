from ImplictTreap import *

def test1():
    ans = 3
    gen = p_Gen()
    a = [1, 1, 1] 
    treap = make(a, gen)
    assert(ans == sum(treap, 1, 3))

def test2():
    ans = 5
    gen = p_Gen()
    a = [1, 1, 1] 
    treap = make(a, gen)
    treap = insert(treap, 4, 4, gen)
    assert(ans == sum(treap, 3, 4))

def test3():
    ans = 42 
    gen = p_Gen()
    a = [1, 1, 42, 1, 1]
    treap = make(a, gen)
    assert(ans == sum(treap,3,3))

def test4():
    ans = 15
    gen = p_Gen()
    a = [1, 2, 42, 3, 4, 5]
    treap = make(a, gen)
    treap = erase(treap, 3)
    assert(ans == sum(treap, 1, 5))
