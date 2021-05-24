# https://leetcode.com/problems/merge-intervals/submissions/
# 56. Merge Intervals
# Medium

# Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, 
# and return an array of the non-overlapping intervals that cover all the intervals in the input.


# Runtime: 88 ms, faster than 47.45% of Python3 online submissions for Merge Intervals.
# Memory Usage: 16.1 MB, less than 82.91% of Python3 online submissions for Merge Intervals.
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        # sort by first index
        
        intervals = sorted(intervals, key=lambda x: x[0])
        
        if not intervals or len(intervals) == 0 or len(intervals) == 1:
            return intervals
        
        ret = [intervals.pop(0)]
        while intervals:
            
            start, end = intervals.pop(0)
            
            if start in range(ret[-1][0], ret[-1][1] + 1):
                
                ret[-1] = [ret[-1][0], max(ret[-1][1], end)]
                
            else:
                ret.append([start,end])
                
        return ret