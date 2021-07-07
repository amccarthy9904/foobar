# https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/
# 378. Kth Smallest Element in a Sorted Matrix
# Medium
# Given an n x n matrix where each of the rows and columns are sorted in ascending order, 
# return the kth smallest element in the matrix.
# Note that it is the kth smallest element in the sorted order, not the kth distinct element.

 

# Runtime: 144 ms, faster than 99.91% of Python3 online submissions for Kth Smallest Element in a Sorted Matrix.
# Memory Usage: 20.2 MB, less than 20.91% of Python3 online submissions for Kth Smallest Element in a Sorted Matrix.
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        flat = [cell for row in matrix for cell in row]
        flat.sort()
        return flat[k-1]