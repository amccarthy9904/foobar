# https://leetcode.com/problems/making-a-large-island/
# 827. Making A Large Island
# Hard
# You are given an n x n binary matrix grid. You are allowed to change at most one 0 to be 1.
# Return the size of the largest island in grid after applying this operation.
# An island is a 4-directionally connected group of 1s.




# Attempt 2:
# for each 0
# swap to 1
# measurte the island size starting at that point
# keep track of largest,return
# faster than attempt 1
# simpler
# still too slow
class Solution:
        
    def largestIsland(self, grid: List[List[int]]) -> int:
        
        def recur(i,j, island):
            
            nonlocal grid
            nonlocal visited
            
            if (i,j) in visited:
                return island
            
            if grid[i][j] == 1:
                island.append((i,j))
                visited.add((i,j))
                
            else:
                return island
        
            if i > 0:
                island = recur(i - 1, j, island)
            if j > 0:
                island = recur(i, j - 1, island)
                
            if i < (len(grid) - 1):
                island = recur(i + 1, j, island)
                
            if j < (len(grid[0]) - 1):
                island = recur(i, j + 1, island)
                
            return island
        
        
        visited = set()
        
        largest = len(recur(0,0, []))
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                
                visited = set()
                
                if grid[i][j] == 0:
                    grid[i][j] = 1
                    largest = max(largest, len(recur(i, j, [])))
                    grid[i][j] = 0
        
        if largest == 0 and grid:
            return 1
        return largest








# Attempt 1:
# identify all islands
# find all border 0's to all islands
# find all common border overlap cells between all islands
# swap overlap cells from 0 to 1, re- mesure size of island
# return largest re-mesured size
# valid solution, takes too ling



class Solution:
        
    def largestIsland(self, grid: List[List[int]]) -> int:
    
        if not grid:
            return 0
        
        islands = {}
        
        visited = set()
        
        def recur(i,j, island):
            
            nonlocal grid
            nonlocal visited
            
            if (i,j) in visited:
                return island
            
            if grid[i][j] == 1:
                island.append((i,j))
                visited.add((i,j))
            else:
                return island
            
            if i > 0:
                island = recur(i - 1, j, island)
            if j > 0:
                island =  recur(i, j - 1, island)
                
            if i < (len(grid) - 1):
                island = recur(i + 1, j, island)
                
            if j < (len(grid[0]) - 1):
                island = recur(i, j + 1, island)
                
            return island

            
        
        for i, row in enumerate(grid):
            for j, cell in enumerate(row):
                
                if (i,j) in visited:
                    continue
                
                if cell == 1:
                    islands[len(islands)] = set(recur(i,j,[]))
                    
                else:
                    visited.add((i,j))
        
        if not islands:
            return 1
        
        
        isl_sizes = {}
        
        
        for island in islands.keys():
            isl_sizes[island] = len(islands[island])
            outside = set()
            
            for coord in islands[island]:
                
                if coord[0] > 0 and grid[coord[0] - 1][coord[1]] == 0 and (coord[0] - 1,coord[1]):
                    outside.add((coord[0] - 1,coord[1]))
                    
                if  coord[1] > 0 and grid[coord[0]][coord[1] - 1] == 0 and (coord[0],coord[1] - 1):
                    outside.add((coord[0],coord[1] - 1))

                if coord[0] < (len(grid) - 1) and grid[coord[0] + 1][coord[1]] == 0 and (coord[0] + 1,coord[1]):
                    outside.add((coord[0] + 1,coord[1]))

                if  coord[1] < (len(grid[0]) - 1) and (coord[0],coord[1] + 1) and grid[coord[0]][coord[1] + 1] == 0:
                    outside.add((coord[0],coord[1] + 1))
            
            islands[island] = outside
        
        keys = islands.keys()
    
        
        largest = max(isl_sizes.values())
        if largest < len(grid) * len(grid[0]):
            largest += 1
        
        for i, island in enumerate(keys):
            
            for cell in islands[island]:
                
                for j in range(i+1, len(keys)):

                    if cell in islands[j]:
                        visited = set()
                        grid[cell[0]][cell[1]] = 1
                        largest = max(largest, len(recur(cell[0], cell[1], [])))
                        grid[cell[0]][cell[1]] = 0
        
        return largest
            

            
                
                
                
        