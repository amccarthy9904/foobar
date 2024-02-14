# https://leetcode.com/problems/two-sum/
# 1. Two Sum
# Easy
# Given an array of integers nums and an integer target
# return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution
# and you may not use the same element twice.

# You can return the answer in any order.

# Runtime 54ms Beats 89.24% of users with Python3
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        d = {}
        for i, num in enumerate(nums):
            t = target - num
            if t in d:
                return [i,d[t]]
            d[num] = i
        