# https://leetcode.com/problems/array-nesting/
# 565. Array Nesting
# Medium

# You are given an integer array nums of length n where nums is a permutation of the numbers in the range [0, n - 1].

# You should build a set s[k] = {nums[k], nums[nums[k]], nums[nums[nums[k]]], ... } subjected to the following rule:

# The first element in s[k] starts with the selection of the element nums[k] of index = k.
# The next element in s[k] should be nums[nums[k]], and then nums[nums[nums[k]]], and so on.
# We stop adding right before a duplicate element occurs in s[k].
# Return the longest length of a set s[k].



# Runtime: 122 ms, faster than 51.97% of Python3 online submissions for Array Nesting.
# Memory Usage: 19.2 MB, less than 35.20% of Python3 online submissions for Array Nesting.

class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        
        max_l = 0
        
        v = set()
        
        for num in nums:
            
            if num in v:
                continue
            
            curr_l = 0
            nxt = num
            
            v2 = {}
            
            while nxt not in v2:
                v2[nxt] = curr_l
                nxt = nums[nxt]
                v.add(nxt)
                curr_l += 1
                
            max_l = max(max_l, curr_l - v2[nxt])
        
        return max_l