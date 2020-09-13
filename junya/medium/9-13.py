class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        ret = [[1 for x in range(n)] for y in range(m)]
        for i in range(1, m):
            for j in range(1, n):
                ret[i][j] = ret[i-1][j] + ret[i][j-1]
        return ret[m-1][n-1]
        
# https://leetcode.com/problems/unique-paths/
