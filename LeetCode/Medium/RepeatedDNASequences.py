# https://leetcode.com/problems/repeated-dna-sequences/submissions/
# 187. Repeated DNA Sequences
# Medium

# The DNA sequence is composed of a series of nucleotides abbreviated as 'A', 'C', 'G', and 'T'.

# For example, "ACGAATTCCG" is a DNA sequence.
# When studying DNA, it is useful to identify repeated sequences within the DNA.

# Given a string s that represents a DNA sequence, return all the 10-letter-long 
# sequences (substrings) that occur more than once in a DNA molecule. You may return the answer in any order.


# Runtime: 60 ms, faster than 78.48% of Python3 online submissions for Repeated DNA Sequences.
# Memory Usage: 27.8 MB, less than 42.12% of Python3 online submissions for Repeated DNA Sequences.
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        
        d = {}
        ret = []
        ind = 10
        
        while ind <= len(s):
            
            nxt = s[ind-10:ind]
            ind += 1
            
            if nxt in d:
                if d[nxt] == 1: continue
                    
                else:
                    d[nxt] = 1
                    ret.append(nxt)
                    
            else: d[nxt] = 0
                
        return ret

# better:
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:

        seen, rep = set(), set()
        for i in range(0, len(s) - 9):
            sub = s[i:i+10]
            if sub in seen:
                rep.add(sub)
            else:
                seen.add(sub)
        return list(rep)