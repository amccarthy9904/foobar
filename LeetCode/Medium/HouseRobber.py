# https://leetcode.com/problems/house-robber/
# 198. House Robber
# Medium
# You are a professional robber planning to rob houses along a street. 
# Each house has a certain amount of money stashed, the only constraint stopping you from 
# robbing each of them is that adjacent houses have security systems connected and 
# it will automatically contact the police if two adjacent houses were broken into on the same night.

# Given an integer array nums representing the amount of money of each house, 
# return the maximum amount of money you can rob tonight without alerting the police.

# Runtime: 24 ms, faster than 96.35% of Python3 online submissions for House Robber.
# Memory Usage: 14.3 MB, less than 49.30% of Python3 online submissions for House Robber.
class Solution:
    def rob(self, nums: List[int]) -> int:
        
        if not nums:
            return 0
        
        if len(nums) <= 2:
            return max(nums)
        
        memo = [nums[0], nums[1]]
        mx = nums[0]
        
        while len(memo) < len(nums):
            
            memo.append(mx + nums[len(memo)])
            mx = max(memo[-2], mx)
            
        return max(mx, memo[-1])