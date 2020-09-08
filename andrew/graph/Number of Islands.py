"""

https://leetcode.com/problems/number-of-islands/

200. Number of Islands

Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

 

Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1
Example 2:

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
"""

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        if grid == []:
            return 0
        
        #Keep track of lands
        countIslands = 0
        #Don't count land already visited again
        setVisited = set()
        
        numCols = len(grid[0])
        numRows = len(grid)
        
        def inGrid(r,c,numRows, numCols):
            if 0 <= r < numRows and 0 <= c < numCols:
                return True
            else:
                return False
        
        for row in range(numRows):
            for col in range(numCols):
                
                if (row, col) not in setVisited and grid[row][col] == "1":
                    #DFS
                    print( (row, col) )
                    stack = [ (row, col) ]
                    while stack:
                        r, c = stack.pop()
                        setVisited.add((r,c))
                        if (r - 1, c) not in setVisited and inGrid(r - 1,c, numRows, numCols) and grid[r-1][c] == "1":
                            stack.append((r-1,c))
                        if (r + 1, c) not in setVisited and inGrid(r + 1,c, numRows, numCols) and grid[r+1][c] == "1":
                            stack.append((r+1,c))
                        if (r, c - 1) not in setVisited and inGrid(r,c - 1, numRows, numCols) and grid[r][c-1] == "1":
                            stack.append((r,c-1))
                        if (r, c + 1) not in setVisited and inGrid(r,c + 1, numRows, numCols) and grid[r][c+1] == "1":
                            stack.append((r,c+1))
                    countIslands += 1
                else:
                    setVisited.add((row,col))
        
        return countIslands