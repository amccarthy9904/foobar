# https://leetcode.com/problems/minimum-genetic-mutation/submissions/
# 433. Minimum Genetic Mutation
# Medium
# A gene string can be represented by an 8-character long string, with choices from 'A', 'C', 'G', and 'T'.

# Suppose we need to investigate a mutation from a gene string start to a gene 
# string end where one mutation is defined as one single character changed in the gene string.

# For example, "AACCGGTT" --> "AACCGGTA" is one mutation.
# There is also a gene bank bank that records all the valid gene mutations. 
# A gene must be in bank to make it a valid gene string.

# Given the two gene strings start and end and the gene bank bank, return the minimum number 
# of mutations needed to mutate from start to end. If there is no such a mutation, return -1.

# Note that the starting point is assumed to be valid, so it might not be included in the bank.

# Runtime: 28 ms, faster than 81.85% of Python3 online submissions for Minimum Genetic Mutation.
# Memory Usage: 14.4 MB, less than 32.38% of Python3 online submissions for Minimum Genetic Mutation.


class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        
        curr = [start]
        nxt  = set()
        steps = 0
        
        while curr:
            
            for g in curr:
                
                if g == end:
                    return steps
                
                for b in bank:
                    
                    diffs = 0
                    for gc, bc in zip(g, b):
                        if gc != bc:
                            diffs += 1
                    
                    if diffs == 1:
                        nxt.add(b)
            
            curr = list(nxt)
            
            for g in nxt:
                bank.remove(g)
                
            nxt = set()
            steps += 1
        
        return -1