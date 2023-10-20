
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        a = [[False for j in range(len(s) + 1)] for i in range(len(p) + 1)]
        a[0][0] = True
        n = len(p)
        m = len(s)
        for i in range(1, n+1):
            for j in range(0, m+1):
                if p[i - 1] == '*':
                    if j == 1: print(a[i-2][j])
                    a[i][j] = a[i-2][j] or ( (j > 0) and (s[j-1] == p[i-2] or p[i-2] == '.') and a[i][j-1])
                else:
                    a[i][j] = (j>0) and (s[j-1] == p[i-1] or p[i-1] == '.') and a[i-1][j-1]
        return a[n][m]
                    
sol = Solution()
p = input('reg> ')
s = input('s> ')
print(sol.isMatch(s, p))
