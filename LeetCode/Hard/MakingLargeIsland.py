# https://leetcode.com/problems/making-a-large-island/
# 827. Making A Large Island
# Hard
# You are given an n x n binary matrix grid. You are allowed to change at most one 0 to be 1.
# Return the size of the largest island in grid after applying this operation.
# An island is a 4-directionally connected group of 1s.

# Attempt 3 -:
# dict islands
# find each island and store all points in set as val in dict
# for each 0 
# sum all islands that 0 touches
# this bad boy is O(n), pretty fast, but bad with space,
# I make an inverse dict called anti_islands that stors cell: island_Key
# there is definatly a better way to do this but thats ok
# Runtime: 3272 ms, faster than 78.99% of Python3 online submissions for Making A Large Island.
# Memory Usage: 77.9 MB, less than 5.16% of Python3 online submissions for Making A Large Island.
class Solution:
    
    def largestIsland(self, grid: List[List[int]]) -> int:
        
        if not grid:
            return 0
        
        islands = {}
        visited = set()

        # dfs that returns list containing tuples of all cell corrds in current island
        def dfs(i,j, island):
            
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
                island = dfs(i - 1, j, island)
            if j > 0:
                island =  dfs(i, j - 1, island)
                
            if i < (len(grid) - 1):
                island = dfs(i + 1, j, island)
                
            if j < (len(grid[0]) - 1):
                island = dfs(i, j + 1, island)
                
            return island

        # create islands dict
        # island_key : set((coord), (coord), ...)
        for i, row in enumerate(grid):
            for j, cell in enumerate(row):
                
                if (i,j) in visited:
                    continue
                
                if cell == 1:
                    islands[len(islands)] = set(dfs(i,j,[]))
                    
                else:
                    visited.add((i,j))
       
        if not islands:
            return 1
        
        anti_island = {}
        
        # create an inverse dict to islands
        # (coord) : island_key 
        for isl in islands.keys():
            for cell in islands[isl]:
                anti_island[cell] = isl
                
        largest = len(islands[0])

        # for every 0 cell
        for i, row in enumerate(grid):
            for j, cell in enumerate(row):
                
                if cell == 0:
                    # sum size  of current cell + all connected islands
                    curr_conn = set()
                    size = 1
                    
                    if i > 0 and (i-1,j) in anti_island and anti_island[(i-1,j)] not in curr_conn:
                        size += len(islands[anti_island[(i-1,j)]])
                        curr_conn.add(anti_island[(i-1,j)])
                        
                    if j > 0 and (i,j-1) in anti_island and anti_island[(i,j-1)] not in curr_conn:
                        size += len(islands[anti_island[(i,j-1)]])
                        curr_conn.add(anti_island[(i,j-1)])
                        

                    if i < (len(grid) - 1) and (i+1,j) in anti_island and anti_island[(i+1,j)] not in curr_conn:
                        size += len(islands[anti_island[(i+1,j)]])
                        curr_conn.add(anti_island[(i+1,j)])
                        
                    if j < (len(grid[0]) - 1) and (i,j+1) in anti_island and anti_island[(i,j+1)] not in curr_conn:
                        size += len(islands[anti_island[(i,j+1)]])
                        curr_conn.add(anti_island[(i,j+1)])
                    
                    largest = max(size, largest)
                    
        return largest

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
            

            
                
                
                
        