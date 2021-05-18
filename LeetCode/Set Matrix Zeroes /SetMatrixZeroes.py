# https://leetcode.com/problems/set-matrix-zeroes/
# Given an m x n matrix. 
# If an element is 0, set its entire row and column to 0. 
# Do it in-place.

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows, cols = {},{}
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    if i not in rows:
                        rows[i] = True
                    if j not in cols:
                        cols[j] = True
                        
        zero_row = [0] * len(matrix[0])
        
        for i in range(len(matrix)):
            if i in rows:
                matrix[i] = zero_row
                
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                
                if j in cols:
                    matrix[i][j] = 0
        