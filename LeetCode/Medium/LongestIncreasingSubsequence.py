# https://leetcode.com/problems/longest-increasing-subsequence/
# 300. Longest Increasing Subsequence
# Medium
# Given an integer array nums, return the length of the longest strictly increasing subsequence.
# A subsequence is a sequence that can be derived from an array by deleting some or no elements
# without changing the order of the remaining elements. For example, [3,6,2,7] is a subsequence of the array [0,3,1,6,2,2,7]

# Solution 1: O(n^2)
# # Runtime: 4352 ms, faster than 14.46% of Python3 submissions
# Memory Usage: 15.1 MB, less than 5.62% of Python3 submissions

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        if not nums:
            return 0
        
        memo = []
        
        for num in nums:
            nxt = 1
            for ind, m in reversed(list(enumerate(memo))):
                if nums[ind] < num:
                    nxt = max(nxt, m+1)
                
            memo.append(nxt)
                
        print(memo)
        return max(memo)


# Solution 2: improved O(n^2) - if we make new max in memo, stop iterating thru memo
# Runtime: 3728 ms, faster than 42.92% of Python3 submissions 
# Memory Usage: 14.9 MB, less than 5.62% of Python3 submissions 
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        if not nums:
            return 0
        
        memo = []
        curr_max = 1
        for num in nums:
            
            nxt = 1
            for ind, m in reversed(list(enumerate(memo))):
                
                if nums[ind] < num:
                    nxt = max(nxt, m+1)
                    if nxt > curr_max:
                        curr_max = nxt
                        break
                        
            memo.append(nxt)
                
        return curr_max

