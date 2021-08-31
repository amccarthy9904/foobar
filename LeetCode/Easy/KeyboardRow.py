# https://leetcode.com/problems/keyboard-row/submissions/

# 500. Keyboard Row
# Easy
# Given an array of strings words, return the words that can be typed using letters 
# of the alphabet on only one row of American keyboard like the image below.

# In the American keyboard:

# the first row consists of the characters "qwertyuiop",
# the second row consists of the characters "asdfghjkl", and
# the third row consists of the characters "zxcvbnm".


# Runtime: 24 ms, faster than 95.69% of Python3 online submissions for Keyboard Row.
# Memory Usage: 14.4 MB, less than 16.83% of Python3 online submissions for Keyboard Row.
class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        row1 = "qwertyuiop"
        row2 = "asdfghjkl"
        row3 = "zxcvbnm"
        
        d = {}
        one_liners = []
        
        for c in row1:
            d[c] = 1
        for c in row2:
            d[c] = 2
        for c in row3:
            d[c] = 3
        
        for word in words:
            
            w = word.lower()
            prev = d[w[0]]
            one_line = True
        
            for c in w:
                
                if d[c] != prev:
                    one_line = False
            
            if one_line:
                one_liners.append(word)
        
        return one_liners