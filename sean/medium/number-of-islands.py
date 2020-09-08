# 9-8-2020
# https://leetcode.com/problems/number-of-islands/

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        if not grid:
            return 0
        
        graph = {}
        self.rows = len(grid)
        self.cols = len(grid[0])
        visited = set()
        count = 0
        
        def get_lands(i, j):
            results = []
            if i != 0 and grid[i - 1][j] == '1':
                results.append((i - 1, j))
            if i != self.rows - 1 and grid[i + 1][j] == '1':
                results.append((i + 1, j))
            if j != 0 and grid[i][j - 1] == '1':
                results.append((i, j - 1))
            if j != self.cols - 1 and grid[i][j + 1] == '1':
                results.append((i, j + 1))
            return results
        
        for i in range(self.rows):
            for j in range(self.cols):
                if grid[i][j] == '0':
                    visited.add((i, j))
                elif (i, j) not in visited:
                    queue = [(i, j)]
                    while queue:
                        land = queue.pop()
                        if land in visited:
                            continue
                        visited.add(land)
                        queue.extend(get_lands(land[0], land[1]))
                    count += 1
        
        return count
