# https://leetcode.com/problems/maximum-subarray/
# 53. Maximum Subarray
# Medium
# Given an integer array nums, find the subarray
# with the largest sum, and return its sum.

# Example 1:

# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: The subarray [4,-1,2,1] has the largest sum 6.

# Runtime 519ms Beats 80.72% of users with Python3
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        max_sum = -sys.maxsize
        curr_sum = 0

        for r in range(0, len(nums)):
            curr_sum += nums[r]
            max_sum = max(max_sum, curr_sum)

            if curr_sum < 1:
                curr_sum = 0
        
        return max_sum

