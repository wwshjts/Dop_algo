from typing import List
class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        m = len(dungeon)
        n = len(dungeon[0])
        a = [[0 for i in range(n)] for j in range(m)]
        a[m-1][n-1] = 1 if dungeon[m-1][n-1] >= 0 else -dungeon[m-1][n-1] + 1
        for i in range(m - 2, -1, -1):
            tmp = a[i + 1][n-1] - dungeon[i][n-1]
            a[i][n-1] = 1 if tmp <= 0 else tmp 
        for j in range(n - 2, -1, -1):
            tmp = a[m-1][j + 1] - dungeon[m-1][j] 
            a[m-1][j] = 1 if tmp <= 0 else tmp

        for i in range(m-2, -1, -1):
            for j in range(n - 2, -1, -1):
                tmp = max(min(a[i+1][j] - dungeon[i][j], 
                            a[i][j+1] - dungeon[i][j]), 1)
                a[i][j] = tmp
        return a[0][0]

s = Solution()

s.calculateMinimumHP([[-2,-3,3],[-5,-10,1],[10,30,-5]])