from typing import List

def dumb(jobs : List[str], deadline : List[int], penalty : List[int]) -> List[str]:
    n = len(jobs)
    deadline = [x - 1 for x in deadline]
    res = [0 for x in range(n)]
    for i in range(n):
        time = deadline[i]
        while (res[time % n] != 0):
            time -= 1
        res[time % n] = jobs[i]
    return res

