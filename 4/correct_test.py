#
#This tes checks alghorithm with unionFind
#

from dumb_solution import dumb
from smart_solution import smart
from random import randint, shuffle

MAX_PEN = 100
MIN_PEN = 10

def make_tst(n):
    jobs = [chr(x) for x in range(ord('A'), ord('A') + n)]
    shuffle(jobs)
    deadline = [x for x in range(1, n + 1)]
    shuffle(jobs) 
    penalty = sorted([randint(MIN_PEN, MAX_PEN) for x in range(n)], reverse = True)
    return jobs, deadline, penalty

def test1():
    jobs = ['D','C','A','E','B']
    deadline = [3,1,3,3,4]
    penalty = [50,30,25,20,10]
    assert smart(jobs, deadline, penalty) == dumb(jobs, deadline, penalty)

def test2():
    jobs = ['D','C','A','E','B']
    deadline = [5,5,5,5,5]
    penalty = [50,30,25,20,10]
    assert smart(jobs, deadline, penalty) == dumb(jobs, deadline, penalty)

def test3():
    for x in range(10):
        test = make_tst(5)
        assert smart(*test) == dumb(*test)
