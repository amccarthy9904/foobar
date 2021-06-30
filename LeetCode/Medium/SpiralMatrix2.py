# https://leetcode.com/problems/spiral-matrix-ii/submissions/
# 59. Spiral Matrix II
# Medium
# Given a positive integer n, generate an n x n matrix filled with elements from 1 to n2 in spiral order


# Runtime: 36 ms, faster than 27.08% of Python3 online submissions for Spiral Matrix II.
# Memory Usage: 14.4 MB, less than 44.45% of Python3 online submissions for Spiral Matrix II.
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        
        mat = []
        
        for i in range(n):
            mat.append([])
            for j in range(n):
                mat[-1].append(0)
        # print(mat)
        curr = 1
        spot = [0,-1]
        d = [1,0,0,0]
        
        while curr <= n ** 2:            
            # print(mat)
            
            if d[0]:
                # print('r')
                s = spot[1] + 1
                if s >= 0 and s < n and mat[spot[0]][s] == 0:
                    spot[1] += 1
                    mat[spot[0]][spot[1]] = curr
                    curr +=1
                
                else:
                    d[0] = 0
                    d[1] = 1
                
            elif d[1]:
                
                # print('d')
                s = spot[0] + 1
                if s >= 0 and s < n and mat[s][spot[1]] == 0:
                    spot[0] += 1
                    mat[spot[0]][spot[1]] = curr
                    curr +=1
                
                else:
                    d[1] = 0
                    d[2] = 1
                
            elif d[2]:
                # print('l')
                
                s = spot[1] - 1
                if s >= 0 and s < n and mat[spot[0]][s] == 0:
                    spot[1] -= 1
                    mat[spot[0]][spot[1]] = curr
                    curr +=1
                
                else:
                    d[2] = 0
                    d[3] = 1
                
                
            elif d[3]:
                # print('u')
                
                s = spot[0] - 1
                if s >= 0 and s < n and mat[s][spot[1]] == 0:
                    spot[0] -= 1
                    mat[spot[0]][spot[1]] = curr
                    curr +=1
                
                else:
                    d[3] = 0
                    d[0] = 1
        return mat