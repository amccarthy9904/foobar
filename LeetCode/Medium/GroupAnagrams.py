# https://leetcode.com/problems/group-anagrams/
# 49. Group Anagrams
# Medium
# Given an array of strings strs, group the anagrams together. 
# You can return the answer in any order.
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, 
# typically using all the original letters exactly once.

# Solution 1: n - num words m - avg len per word O(n(mlog(m)))
# Runtime: 96 ms, faster than 76.94% of Python3 submissions 
# Memory Usage: 17.3 MB, less than 71.69% of Python3 submissions 

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        s2 = [''.join(sorted(w)) for w in strs]
        
        fin = []
        d = {}
        for ind, w in enumerate(s2):
            
            if w not in d:
                d[w] = len(fin)
                fin.append([strs[ind]])
            else:
                fin[d[w]].append(strs[ind])
        
        return fin
                    