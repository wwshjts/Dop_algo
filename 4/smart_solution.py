from typing import List

class UnionFind:
    def __init__(self, elems : List[int]):
        self.items = elems.copy()
        self.par = [x for x in range(len(elems))]
        self.rank = [0 for x in range((len(elems)))]

    def inner_find(self, u : int) -> int:
        if self.par[u] != u:
            self.par[u] = self.inner_find(self.par[u])
        return self.par[u] 
    
    def find(self, u):
        return self.items[self.inner_find(u)]
    
    def union(self, u : int, v : int):
        a = self.inner_find(u)
        b = self.inner_find(v)
        if self.rank[a] > self.rank[b]:
            self.par[b] = a 
        if self.rank[a] < self.rank[b]:
            self.par[a] = b
            #При слиянии объявлем представителем представителя левого класса
            self.swap(a, b)
        if self.rank[a] == self.rank[b]:
            self.par[b] = a
            self.rank[a] += 1

    
    def swap(self, i, j):
        self.items[i], self.items[j] = self.items[j], self.items[i]

    def is_root(self, u : int) -> bool:
        return self.par[u] == u
    
    def print(self):
        for i in range(len(self.items)):
            print(f'index: {i}; item {self.items[i]}; class_index {self.inner_find(i)}; class_item {self.find(i)}')

def smart(jobs : List[str], deadline : List[int], penalty : List[int]) -> List[str]:
    n = len(jobs)
    deadline = [x - 1 for x in deadline]
    res = [0 for x in range(n)]
    uf = UnionFind([x for x in range(0, n)])

    for i in range(n):
        time = uf.find(deadline[i]) % n 
        res[time] = jobs[i]
        uf.union((time - 1) % n, time)
        if res[(time + 1) % n] != 0:
            uf.union(time, (time + 1) % n)

    return res
    
print(smart(['D','C','A','E','B'], [3,1,3,3,4], [50,30,25,20,10]))


