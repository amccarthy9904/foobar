https://leetcode.com/problems/length-of-last-word/
58. Length of Last Word
Easy
Given a string s consists of some words separated by spaces, 
return the length of the last word in the string. If the last word does not exist, return 0.

A word is a maximal substring consisting of non-space characters only.

# Sol 1
# Runtime: 28 ms, faster than 81.31% of Python3 submissions
# Memory Usage: 14.4 MB, less than 34.75% of Python3 submissions
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.rstrip()
        for i in range(len(s)-1, -1, -1):
            
            if s[i] == " ":
                return len(s)-1 - i
            
        return len(s)