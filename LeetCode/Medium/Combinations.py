# https://leetcode.com/problems/combinations/submissions/
# 77. Combinations
# Medium
# Given two integers n and k, 
# return all possible combinations of k numbers out of the range [1, n].

# You may return the answer in any order.


# Solution 1: kinda jank
# # Runtime: 456 ms, faster than 70.38% of Python3 online submissions for Combinations.
# # Memory Usage: 15.8 MB, less than 23.80% of Python3 online submissions for Combinations.

class Solution:
    picks = None
    
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        
        def gen(ind, k, l):
            
            if l == k:
                return [[self.picks[ind]]]
            
            ret = []
            for i in range(ind+1, n):
                
                x = gen(i, k, l+1)
                for lst in x:
                    lst.append(self.picks[ind])
                ret += x
                
            return ret
        
        self.picks = [c for c in range(1, n+1)]
        
        
        r = []
        for i in range(n):
            r += gen(i, k, 1)
        return r
            