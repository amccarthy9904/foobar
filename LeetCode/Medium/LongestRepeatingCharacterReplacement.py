# https://leetcode.com/problems/longest-repeating-character-replacement/
# 424. Longest Repeating Character Replacement
# Medium
# You are given a string s and an integer k. You can choose any character of the string 
# and change it to any other uppercase English character. 
# You can perform this operation at most k times.

# Return the length of the longest substring containing 
# the same letter you can get after performing the above operations.

# Runtime 70ms Beats 94.75% of users with Python3
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        max_freq, l = 0, 0
        freq = {}

        for r in range(len(s)):

            if s[r] not in freq: freq[s[r]] = 1
            else: freq[s[r]] += 1
            
            if r - l > max_freq + k:
                freq[s[l]] -= 1
                l += 1
            
            max_freq = max(max_freq, freq[s[r]])
        
        return min(max_freq + k, len(s))
            
