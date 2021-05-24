# 200. Number of Islands
# Medium

# Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), 
# return the number of islands.
# An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. 
# You may assume all four edges of the grid are all surrounded by water.

# Runtime: 140 ms, faster than 65.74% of Python3 online submissions for Number of Islands.
# Memory Usage: 22.7 MB, less than 5.11% of Python3 online submissions for Number of Islands.
class Solution:
    def numIslands(self, grid: [[str]]) -> int:
        # m, n = len(grid), len(grid[0])
        visited = {}
        num = 0

        def map_land(m, n):
            if (m + 1, n) not in visited and m + 1 < len(grid):
                if grid[m + 1][n] == "1":
                    visited[(m + 1, n)] = True
                    map_land(m + 1, n)

            if (m - 1, n) not in visited and m - 1 > -1:
                if grid[m - 1][n] == "1":
                    visited[(m - 1, n)] = True
                    map_land(m - 1, n)

            if (m, n - 1) not in visited and n - 1 > -1:
                if grid[m][n - 1] == "1":
                    visited[(m, n - 1)] = True
                    map_land(m, n - 1)

            if (m, n + 1) not in visited and n + 1 < len(grid[0]):
                if grid[m][n + 1] == "1":
                    visited[(m, n + 1)] = True
                    map_land(m, n + 1)

        for m in range(len(grid)):
            for n in range(len(grid[0])):
                if (m, n) in visited:
                    continue

                else:
                    visited[(m, n)] = True
                    if grid[m][n] == "1":
                        num += 1
                        map_land(m, n)
        return num

    def test(self):
        grid1 = [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]
        grid2 = [["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]
        print("grid1")
        for row in grid1:
            print(row)
        print("Result: " + str(self.numIslands(grid1)) + "\nExpected: 1")


        print("grid2")
        for row in grid2:
            print(row)
        print("Result: " + str(self.numIslands(grid2)) + "\nExpected: 3")

numIs = Solution()
numIs.test()
