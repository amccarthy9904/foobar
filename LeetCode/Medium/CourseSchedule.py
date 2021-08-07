# https://leetcode.com/problems/course-schedule/submissions/
# 207. Course Schedule
# Medium

# There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. 
# You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates 
# that you must take course bi first if you want to take course ai.

# For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
# Return true if you can finish all courses. Otherwise, return false.



# Runtime: 96 ms, faster than 77.55% of Python3 online submissions for Course Schedule. 
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        d = {}
        
        for pre, post in prerequisites:
            
            if post not in d:
                d[post] = [pre]
            else:
                d[post].append(pre)
        
        start = set([i for i in range(numCourses) if i not in d])
        prev_l = -1
        
        while prev_l != len(start) and d:
            
            prev_l = len(start)
            keys = list(d.keys())
            
            for k in keys:
                
                if k in start:
                    del d[k]
                    continue
                
                pre_requs_met = True
                
                for v in d[k]:
                    if v not in start:
                        pre_requs_met = False
                        break
                
                if pre_requs_met:
                    start.add(k)
                    del d[k]
         
        return len(start) == numCourses
        