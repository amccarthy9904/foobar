# https://leetcode.com/problems/unique-paths/
# 62. Unique Paths
# Medium
# A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).
# The robot can only move either down or right at any point in time. The robot is trying to reach 
# the bottom-right corner of the grid (marked 'Finish' in the diagram below).
# How many possible unique paths are there?

# Sol1: pretty good
# Runtime: 24 ms, faster than 96.18% of Python3 submissions
# Memory Usage: 14.4 MB, less than 13.25% of Python3 submissions
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        grid = [[0 for x in range(n)] for y in range(m)]
        
        grid[0][0] = 1 
        
        for r, row in enumerate(grid):
            for c, cell in enumerate(row):
                
                if c == 0 and r == 0:
                    continue
                    
                cell = 0
                
                if c > 0:
                    cell += row[c-1]
                if r > 0:
                    cell += grid[r-1][c]
                grid[r][c] = cell
                
        return grid[-1][-1]

