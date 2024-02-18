# https://leetcode.com/problems/longest-substring-without-repeating-characters/
# 3. Longest Substring Without Repeating Characters
# Medium
# Given a string s, find the length of the longest substring without repeating characters.

# front and back pointers
# iterate through list, when front hits end of list stop
# iterate front
# sl = slice from back to front 
# if len(sl) = len(set(sl))
#   iterate front, continue
# else 
#    iterate back, continue
# keep track of max diff between front and back
# return at end

# First attempt, slow 
# Runtime: 240 ms, faster than 22.43% of Python3 online submissions
# Memory Usage: 14.3 MB, less than 54.16% of Python3 online submissions
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        front, back = 0, 0
        longest = 0
        
        if not s or s == '':
            return 0
        
        while front <= len(s):
            
            sub = s[back:front]
            
            if len(sub) == len(set(sub)):
                
                longest = max(longest, len(sub))
                front +=1
            else:
                back += 1
        
        return longest

# First attempt, Iteration 2, Faster 
# Runtime: 92 ms, faster than 28.85% of Python3 online submissions for Longest Substring Without Repeating Characters.
# Memory Usage: 14.2 MB, less than 79.64% of Python3 online submissions for Longest Substring Without Repeating Characte
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        front, back = 1, 0
        longest = 0
        
        if not s or s == '':
            return 0
        
        while front <= len(s):
            
            sub = s[back:front]
            if sub.index(sub[-1]) == len(sub) -1:
                
                longest = max(longest, len(sub))
                front +=1
            else:
                back += sub.index(sub[-1]) + 1
        
        return longest



# Best Solution, dictionary stores all unique chars and their most recently visited index
# iterate ind, if s[ind] in d, substring start index set to index of d[s[ind]] + 1, update d
# Runtime: 52 ms, faster than 90.61% of Python3 online submissions for Longest Substring Without Repeating Characters.
# Memory Usage: 14.1 MB, less than 93.11% of Python3 online submissions for Longest Substring Without Repeating Characters.
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        if not s or len(s) == 0:
            return 0
        if len(s) == 1:
            return 1
        
        d = {}
        start = 0
        longest = 0
        
        for ind, c in enumerate(s):

            if c in d and start <= d[c]:
                start = d[c] + 1
            else:
                longest = max(longest, (ind - start) + 1)

            d[c] = ind
        
        return longest
    

# a good revision:
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        ret,l = 0, -1
        d = {}
        for r, c in enumerate(s):

            if c in d and d[c] > l:
                l = d[c]
            d[c] = r
            ret = max(ret, r-l)
        return ret
        
# another try
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:


        if len(s) < 2:
            return len(s)
        
        seen = {s[0]:0}
        ret = 0
        l = 0
        for r in range(1, len(s)):
            if s[r] in seen:
                done = False
                while not done:
                    done = s[l] == s[r]
                    del seen[s[l]]
                    l += 1
            
            ret = max(ret, r - l+1)
            seen[s[r]] = r
        return ret

        