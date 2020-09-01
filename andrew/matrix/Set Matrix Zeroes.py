"""
https://leetcode.com/problems/set-matrix-zeroes/
73. Set Matrix Zeroes (Medium)

Given an m x n matrix. If an element is 0, set its entire row and column to 0. Do it in-place.

Follow up:

A straight forward solution using O(mn) space is probably a bad idea.
A simple improvement uses O(m + n) space, but still not the best solution.
Could you devise a constant space solution?
 

Example 1:


Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]
Example 2:


Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
 

Constraints:

m == matrix.length
n == matrix[0].length
1 <= m, n <= 200
-10^9 <= matrix[i][j] <= 10^9
"""
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        listCol = set()
        listRow = set()
        
        #O(n^2)
        for i in range(0, len(matrix)):
            for j in range(0, len(matrix[i])):
                if matrix[i][j] == 0:
                    listCol.add(j)
                    listRow.add(i)
        
        for i in listRow:
            for e in range(0, len(matrix[i])):
                matrix[i][e] = 0
        
        for i in listCol:
            for e in range(0, len(matrix)):
                matrix[e][i] = 0
        
        return matrix