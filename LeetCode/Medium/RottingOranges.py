# https://leetcode.com/problems/rotting-oranges/
# 994. Rotting Oranges
# Medium
# You are given an m x n grid where each cell can have one of three values:

# 0 representing an empty cell,
# 1 representing a fresh orange, or
# 2 representing a rotten orange.
# Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

# Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.



# Runtime: 52 ms, faster than 71.01% of Python3 online submissions for Rotting Oranges.
# Memory Usage: 14.3 MB, less than 36.33% of Python3 online submissions for Rotting Oranges.
class Solution:
    
    
    def get4dirs(self, grid, start):
        
        coords = []
        
        if start[0] > 0:
            coords.append([start[0]-1, start[1]])
        if start[1] > 0:
            coords.append([start[0], start[1]-1])
        if start[0] < len(grid) - 1:
            coords.append([start[0]+1, start[1]])
        if start[1] < len(grid[0]) - 1:
            coords.append([start[0], start[1]+1])
        return coords
        
        
    
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        rottens = []
        freshes = []
        
        for rind, row in enumerate(grid):
            for cind, cell in enumerate(row):
                if cell == 2:
                    rottens.append([rind,cind])
                elif cell == 1:
                    freshes.append([rind,cind])
        
        if not freshes:
            return 0
            
        nxt = []
        time = 0
        while rottens:
            
            curr = rottens.pop()
            coords = self.get4dirs(grid, curr)
            
            for coord in coords:
                if grid[coord[0]][coord[1]] == 1:
                    freshes.remove(coord)
                    grid[coord[0]][coord[1]] = 2
                    nxt.append(coord)
            
            if not rottens:
                rottens = nxt
                nxt = []
                time += 1
        
        if not freshes:
            return time - 1
        return -1
                    
            
            