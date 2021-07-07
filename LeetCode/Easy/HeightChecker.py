# https://leetcode.com/problems/height-checker/
# 1051. Height Checker
# Easy

# A school is trying to take an annual photo of all the students.
# The students are asked to stand in a single file line in non-decreasing order by height. 
# Let this ordering be represented by the integer array expected where expected[i] is the expected height of the ith student in line.

# You are given an integer array heights representing the current order 
# that the students are standing in. Each heights[i] is the height of the ith student in line (0-indexed).

# Return the number of indices where heights[i] != expected[i].

# Runtime: 32 ms, faster than 87.27% of Python3 online submissions for Height Checker.
# Memory Usage: 14.2 MB, less than 41.76% of Python3 online submissions for Height Checker.
class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        
        if not heights or len(heights) == 1:
            return 0
        
        expected = sorted(heights)
        total = 0
        
        for ind in range(len(heights)):
            
            if expected[ind] != heights[ind]:
                total += 1
        
        return total