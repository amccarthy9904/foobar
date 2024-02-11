# https://leetcode.com/problems/palindromic-substrings/description/?envType=daily-question&envId=2024-02-11
# 647. Palindromic Substrings
# Medium
# Given a string s, return the number of palindromic substrings in it.
# A string is a palindrome when it reads the same backward as forward.
# A substring is a contiguous sequence of characters within the string.

# Runtime 82ms Beats 64.93% of users with Python3
class Solution:
    def countSubstrings(self, s: str) -> int:
        # for each s[i]
        # find all palindromes whose middle is s[i]
        # find all aplindromes whose middle is s[i-1]s[i]
        found = 0
        def check(i, j, s):
            mod = 0
            found = 0
            while j - mod >= 0 and i + mod < len(s):
                if s[j-mod] == s[i+mod]:
                    found += 1
                else:
                    break
                mod += 1
            return found
                    
        for i, c in enumerate(s):    
            
            found += check(i,i,s)
            if i > 0: found += check(i,i-1,s)
                
        return found