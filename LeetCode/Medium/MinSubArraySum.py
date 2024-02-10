# https://leetcode.com/problems/minimum-size-subarray-sum/description/
# 209. Minimum Size Subarray Sum
# Medium

# Given an array of positive integers nums and a positive integer target
# return the minimal length of a subarray
#  whose sum is greater than or equal to target. 
# If there is no such subarray, return 0 instead.

# time O(n) - space O(1)
# Runtime 186ms Beats 94.36% of users with Python3
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        min_len = len(nums) + 1

        l = -1
        curr_sum = 0

        for r, num in enumerate(nums):
            curr_sum += num
            
            while curr_sum >= target:
                min_len = min(min_len, r - l)
                l+=1
                curr_sum -= nums[l]
            
        if min_len > len(nums):
            return 0
        return min_len