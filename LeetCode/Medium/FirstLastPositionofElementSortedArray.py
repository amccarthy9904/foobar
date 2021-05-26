
# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
# 34. Find First and Last Position of Element in Sorted Array
# Medium
# Given an array of integers nums sorted in ascending order, 
# find the starting and ending position of a given target value.
# If target is not found in the array, return [-1, -1].
# You must write an algorithm with O(log n) runtime complexity

# Solution 1: 
# # Runtime: 84 ms, faster than 68.91% of Python3 submissions
# Memory Usage: 15.5 MB, less than 48.21% of Python3 submissions
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        if len(nums) == 1:
            
            if nums[0] == target:
                return [0,0]
            else:
                return [-1,-1]
        
        try:
            start = nums.index(target)
            
            for i in range(start, len(nums)):
                if nums[i] != nums[start]:
                    return [start, i - 1]
            
            return [start,len(nums)-1]

        except:
            # target not in nums
            return [-1, -1]