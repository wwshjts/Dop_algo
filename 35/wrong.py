from typing import List
from smart_solution import smart
from random import randint, shuffle

MIN_PEN = 10
MAX_PEN = 100

def wrong(jobs : List[str], deadline : List[int], penalty : List[int]) -> List[str]:
    return jobs

def make_tst(n):
    jobs = [chr(x) for x in range(ord('A'), ord('A') + n)]
    shuffle(jobs)
    deadline = [randint(1, n) for x in range(1, n + 1)]
    shuffle(deadline) 
    penalty = sorted([randint(MIN_PEN, MAX_PEN) for x in range(n)], reverse = True)
    return jobs, deadline, penalty

def sol_sum(sol, jobs, deadline, penalty):
    index = {jobs[i] : i for i in range(len(jobs))} 
    res = 0
    for i in range(len(sol)):
        job = sol[i]
        if deadline[index[job]] > i + 1:
            res += penalty[index[job]]
    return res

def test():
    test = make_tst(5)
    jobs, deadline, penalty = test
    ans_cor = smart(*test) 
    ans_wrong = wrong(*test)
    print(f'smart {sol_sum(ans_cor, *test)} naive {sol_sum(ans_wrong, *test)}')


for i in range(10):
    test()
